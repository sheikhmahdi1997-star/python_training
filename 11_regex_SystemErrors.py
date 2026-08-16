import re

log_data = """2026-08-04 10:15:32 INFO User logged in
2026-08-04 10:16:01 ERROR 404 User not found - /api/profile
2026-08-04 10:17:45 ERROR 500 Internal Server Error - /database/connection
2026-08-04 10:18:12 DEBUG Cache cleared
2026-08-04 10:19:55 ERROR 403 Forbidden access - /admin/panel
2026-08-04 10:20:33 INFO Request completed"""


pattern = r"ERROR (\d{3}) (.+?) - (/.+)"


matches = re.findall(pattern, log_data)


errors = []
for status, message, uri in matches:
    errors.append({
        "status": status,
        "uri": uri,
        "message": message
    })

print(errors)