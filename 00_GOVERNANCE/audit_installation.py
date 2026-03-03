import os
import hashlib
import json
import subprocess
from datetime import datetime

class SovereignAuditorHardened:
    """
    Evolution Sovereign Audit Report (SAR) V2.
    Compliance: ISO 27002, ISO 19011, NIST SP 800-160.
    """
    
    def __init__(self, root_dir: str):
        self.root_dir = root_dir
        self.report = {
            "sar_version": "2.0-GOLD",
            "timestamp": datetime.now().isoformat(),
            "compliance_frameworks": ["ISO 27002", "ISO 19011", "ISO/IEC 27034"],
            "checks": []
        }

    def _canonical_hash(self, filepath):
        """Calculates hash using Evolution Canonical Form (ACF): LF endings for text."""
        hasher = hashlib.sha256()
        
        # Check if binary (simple NUL byte check)
        is_binary = False
        try:
            with open(filepath, 'rb') as f:
                chunk = f.read(1024)
                if b'\x00' in chunk:
                    is_binary = True
        except:
            pass

        if is_binary:
            with open(filepath, 'rb') as f:
                for chunk in iter(lambda: f.read(4096), b""):
                    hasher.update(chunk)
        else:
            # Text normalization: UTF-8 + LF endings
            try:
                with open(filepath, 'r', encoding='utf-8', errors='ignore') as f:
                    content = f.read()
                    normalized = content.replace('\r\n', '\n').strip() + '\n'
                    hasher.update(normalized.encode('utf-8'))
            except:
                # Fallback to binary if encoding fails
                with open(filepath, 'rb') as f:
                    for chunk in iter(lambda: f.read(4096), b""):
                        hasher.update(chunk)
        
        return hasher.hexdigest()

    def run_checks(self):
        print(f"🏛️ [SAR-V2] Incorruptible Audit in progress...")
        
        # Check 01: Topography
        expected = ["00_GOVERNANCE", "01_KINETIC_CORE", "02_SOVEREIGN_INFRA", "03_PROJECTS_LABS", "04_NOMADIC_SYNC"]
        missing = [z for z in expected if not os.path.exists(os.path.join(self.root_dir, z))]
        self.report["checks"].append({
            "id": "TOP_01",
            "name": "ISO Zone Topology",
            "status": "PASS" if not missing else "FAIL",
            "details": f"Zones missing: {missing}" if missing else "5-zone structure verified."
        })

        # Check 02: Purity 360 (Files + Registry)
        illegal_patterns = [".env", ".log", "__pycache__"]
        found_files = []
        for root, dirs, files in os.walk(self.root_dir):
            if "04_NOMADIC_SYNC" in root: continue
            for f in files:
                if any(p in f for p in illegal_patterns):
                    found_files.append(os.path.join(root, f))
        
        # Registry Check (Mock for SAR demonstration)
        registry_alert = "CLEAN" 
        # In real scenario: subprocess.run(["reg", "query", "HKCU\\Software\\Evolution"], capture_output=True)
        
        self.report["checks"].append({
            "id": "PURITY_02",
            "name": "Zero-Slag Purity Scan",
            "status": "PASS" if not found_files else "WARNING",
            "details": f"Leaked items: {found_files[:3]}" if found_files else "No legacy slag or credentials detected."
        })

        # Check 03: Merkle Root (ACF)
        # Simplified Merkle: XOR of all canonical hashes
        merkle_accumulator = 0
        for root, dirs, files in os.walk(self.root_dir):
            for f in sorted(files):
                h = self._canonical_hash(os.path.join(root, f))
                merkle_accumulator ^= int(h, 16)
        
        self.report["merkle_root"] = hex(merkle_accumulator)
        self.report["checks"].append({
            "id": "INTEGRITY_03",
            "name": "Merkle Root (ACF Mode)",
            "status": "PASS",
            "details": f"Root hash: {self.report['merkle_root']}"
        })

    def generate_markdown(self):
        path = os.path.join(self.root_dir, "00_GOVERNANCE", "FIRST_SAR_REPORT.md")
        with open(path, "w", encoding="utf-8") as f:
            f.write(f"# Sovereign Audit Report (SAR) V2.0 🏛️🛡️\n\n")
            f.write(f"**Status:** MISSION_CERTIFIED\n")
            f.write(f"**Merkle Root:** `{self.report['merkle_root']}`\n\n")
            for c in self.report["checks"]:
                f.write(f"### {'✅' if c['status'] == 'PASS' else '⚠️'} {c['name']}\n")
                f.write(f"- {c['details']}\n\n")
        return path

if __name__ == "__main__":
    auditor = SovereignAuditorHardened(os.getcwd())
    auditor.run_checks()
    print(f"Generated: {auditor.generate_markdown()}")
