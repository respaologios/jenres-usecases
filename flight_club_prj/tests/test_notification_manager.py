import pytest
from unittest.mock import Mock, patch
from flight_club_prj.notification_manager import NotificationManager


class TestNotificationManager:

    @patch('flight_club_prj.notification_manager.Client')
    def test_send_sms(self, mock_client):
        # Setup
        notification_manager = NotificationManager()
        mock_client_instance = mock_client.return_value
        mock_client_instance.messages.create.return_value.sid = 'SMtestsid'

        # Exercise
        sid = notification_manager.send_sms('Test Message')

        # Verify
        assert sid == 'SMtestsid'
        mock_client_instance.messages.create.assert_called_once_with(
            body='Test Message',
            from_=ANY,
            to=ANY,
        )

    @patch('flight_club_prj.notification_manager.smtplib.SMTP')
    def test_send_emails(self, mock_smtp):
        # Setup
        notification_manager = NotificationManager()
        mock_smtp_instance = mock_smtp.return_value
        mock_smtp_instance.starttls.return_value = None
        mock_smtp_instance.login.return_value = None
        mock_smtp_instance.sendmail.return_value = {}

        # Exercise
        notification_manager.send_emails(['test@example.com'], 'Test Message')

        # Verify
        mock_smtp_instance.starttls.assert_called_once()
        mock_smtp_instance.login.assert_called_once_with(ANY, ANY)
        mock_smtp_instance.sendmail.assert_called_once_with(
            from_addr=ANY,
            to_addrs='test@example.com',
            msg=ANY
        )
