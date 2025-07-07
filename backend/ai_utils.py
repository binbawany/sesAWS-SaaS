def generate_email(name):
    subject = f"Let's connect, {name}"
    body = f"Hi {name},\n\nThis is an AI-generated email to reach out about our services."
    return subject, body