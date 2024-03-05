import vonage

client = vonage.Client(key="3a703bb0", secret="r0o0xa0qWlMLxVxe")
sms = vonage.Sms(client)

responseData = sms.send_message(
    {
        "from": "Vonage Sample",
        # "to": "6285281944451",
        "to": "6285157145443",
        "text": "A text message sent using the Vonage SMS API",
    }
)

if responseData["messages"][0]["status"] == "0":
    print("Message sent successfully.")
else:
    print(f"Message failed with error: {responseData['messages'][0]['error-text']}")