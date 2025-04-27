from celery import shared_task

@shared_task
def dummy_background_task(name, email):
    print(f"Task started for {name} with email {email}")
