# ── hooks/post_gen_project.py ─────────────────────────────────────────────
"""
After Cookiecutter renders the project, this hook injects a creation
timestamp and a fresh UUID into config/experiment.toml and README.md.
"""
import datetime as _dt
import pathlib as _p
import re, uuid

def _patch(file_path: str, replacements: dict):
    path = _p.Path.cwd() / file_path
    if not path.exists():
        return
    content = path.read_text(encoding="utf-8")
    for pattern, replacement in replacements.items():
        content = re.sub(pattern, replacement, content)
    path.write_text(content, encoding="utf-8")

def _patch_readme(file_path: str):
    # Agregar UUID y fecha a línea 5 de README.md
    readme = _p.Path.cwd() / file_path
    if readme.exists():
        lines = readme.read_text(encoding="utf-8").splitlines()
        if len(lines) >= 4:
            created = _dt.datetime.now().isoformat(timespec="seconds")
            uid = str(uuid.uuid4())
            lines.insert(4, f"Created on: {created}\nUUID: {uid}")
            readme.write_text('\n'.join(lines), encoding="utf-8")

_subs = {
    r'created\s*=\s*".*?"': f'created = "{_dt.datetime.now().isoformat(timespec="seconds")}"',
    r'uuid\s*=\s*".*?"': f'uuid = "{uuid.uuid4()}"',
    r'\{\{\s*cookiecutter\.creation_date\s*\}\}': _dt.datetime.now().isoformat(timespec="seconds"),
    r'\{\{\s*cookiecutter\.experiment_id\s*\}\}': str(uuid.uuid4())
}
try:
    print("✅ Hook is running!")
    print("PATCHING: experiment.toml and README.md")

    _patch("config/experiment.toml", _subs)
    _patch_readme("README.md")
except Exception as e:
    print(f"[HOOK ERROR] {e}")
# ──────────────────────────────────────────────────────────────────────────
