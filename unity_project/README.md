### Hi, thanks for the test, I really enjoy working on it.

## Installation and Running
In unity_project subfolder
- `python -m venv venv`
- Activate virtual environment `venv\Scripts\activate.bat` (Windows) or `source venv/bin/activate` in Mac
- `pip install -r requirements.txt`
- `python manage.py runserver`

- Check http://localhost:8000/ for the view to display all emails and statistics
- Can test submit email at http://localhost:8000/leads

## Model
Email table, I have these columns:
- email: the real email (must be unique and not blank).
- created_at: the time when email submitted to our system.
- verified_at: the time when user verify the email.
- unsubscribed_at: the time when user unsubscribe from the list.

## Assumptions
- Email list, I get all emails subscribed.
- New this month, I count emails that are created on this month (use created_at column).
- Unsubscribed, I count all emails that are unsubscribed.

## Celery tasks
I also created celery tasks that scheduled to run on Monday and Wednesday


I am looking forward to hearing from you.

Best regards,<br/>
Tra Thanh Lan



