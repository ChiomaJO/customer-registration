import json


def lambda_handler(event, context):

    body = event.get("body", "{}")

    try:
        data = json.loads(body)
    except json.JSONDecodeError:
        return response(
            400,
            "Invalid request data."
        )

    full_name = data.get("fullName", "").strip()
    email = data.get("email", "").strip()
    phone = data.get("phone", "").strip()
    date_of_birth = data.get("dateOfBirth", "").strip()
    gender = data.get("gender", "").strip()
    address = data.get("address", "").strip()

    if not full_name:
        return response(400, "Please enter your full name.")

    if not email:
        return response(400, "Please enter your email address.")

    if "@" not in email or "." not in email:
        return response(400, "Please enter a valid email address.")

    if not phone:
        return response(400, "Please enter your phone number.")

    if not date_of_birth:
        return response(400, "Please enter your date of birth.")

    if not gender:
        return response(400, "Please select your gender.")

    if not address:
        return response(400, "Please enter your address.")

    return response(
        200,
        "Customer information received successfully!"
    )


def response(status_code, message):

    return {
        "statusCode": status_code,
        "headers": {
            "Content-Type": "application/json"
        },
        "body": json.dumps({
            "message": message
        })
    }