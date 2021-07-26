# Price-Alert-Application


Price Alert Application

It Allows User to Create a price alert  that triggers a notification via email when the user’s target price is achieved.

API endpoints:

'alerts/create/' - rest api endpoint for user’s to create an alert.


'alerts/id/ - rest api endpoint for user's to fetch alert by using id.


'alerts/id/delete/' - rest api endpoint for user's to delete an alert.


'alerts/all_alerts/' - rest api endpoint to fetch all the alerts that the user has created including the status of the alerts.


'alerts/created_alerts/' - rest api endpoint to fetch alerts that were created.


'alerts/deleted_alerts/' - rest api endpoint to fetch alerts that were deleted.


'alerts/triggered_alerts/' - rest api endpoint to fetch alerts that were triggered.


'alerts/applyalerts/' - rest api endpoint to check the user's target price and send the notification.


But before using these api's user must register using 'alerts/register/' if there is no account else can login using 'alerts/login/'.


Features:

 - >  User authentication to api endpoints.
 - >  Paginated the response.
 - >  Sends notification via email.


