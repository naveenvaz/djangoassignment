from django.core.management.base import BaseCommand
from django.core.mail import send_mail
from django.utils import timezone
from todoapp.models import TodoTask
from django.template.loader import render_to_string

class Command(BaseCommand):
    help = 'Send reminders for upcoming tasks'

    def handle(self, *args, **options):
        tasks = TodoTask.objects.filter(deadline__gt=timezone.now())
        no_reminder_sent = True

        for task in tasks:
            time_until_deadline = task.deadline - timezone.now()
            if time_until_deadline.total_seconds() <= 3600:
                subject = f"Reminder: Task '{task.name}'"
                body = render_to_string('todoapp/reminder_email.html', {'task': task, 'username': task.user.username})
                send_mail(subject, body, 'naveenvaz100@example.com', [task.user.email], html_message=body)
                self.stdout.write(self.style.SUCCESS(f'Reminder sent for Task "{task.name}" to {task.user.email}'))
                no_reminder_sent = False

        if no_reminder_sent:
            self.stdout.write(self.style.SUCCESS('No reminder emails to send for any tasks'))

        self.stdout.write(self.style.SUCCESS('Reminders processed successfully!'))
