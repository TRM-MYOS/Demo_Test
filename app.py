def check_access(is_admin):
    assert is_admin  # B101 (LOW -5): ใช้ assert ตรวจสิทธิ์
    try:
        return True
    except Exception:
        pass 