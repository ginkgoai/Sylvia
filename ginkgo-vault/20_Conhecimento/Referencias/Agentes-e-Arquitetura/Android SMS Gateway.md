---
title: "Android SMS Gateway"
source: "https://textbee.dev/"
author:
  - "[[Israel Abebe Kokiso]]"
published:
created: 2026-06-27
description: "Send SMS messages programmatically from your applications using your Android device. No SMS gateway fees, simple API, and powerful integrations."
tags:
  - "clippings"
---
98%

Cost savings vs. traditional SMS gateways

3 min

Average setup time

1M+

Messages sent per month

Open source

Transparent and self-hostable

Features

## Everything you need to send & receive SMS

Send and receive SMS online with your Android phone. Simple API, webhooks, and bulk messaging. Learn how to [send SMS](https://textbee.dev/docs/sending-sms/sending-sms) or [receive SMS](https://textbee.dev/docs/receiving-sms) in the docs, or try our [SMS tools](https://textbee.dev/tools).

### SMS API

Send SMS from any app with a single REST call. No SDKs to wrestle, no vendor lock-in, and it works with Node, Python, cURL, or anything that speaks HTTP.

[Read the send docs](https://textbee.dev/docs/sending-sms/sending-sms)

### Receive SMS Online

Receive inbound texts via webhooks or the API. Build OTP verification, support inboxes, and true two-way messaging.

[Read the receive docs](https://textbee.dev/docs/receiving-sms)

### Bulk Messaging

Reach many recipients in a single API call: campaigns, alerts, and broadcasts without writing loops.

### SMS Templates

Reusable templates with dynamic variables so your team ships consistent messages faster.

### Advanced Analytics

See delivery, volume, and performance at a glance with detailed reports.

### Multi-Device Support

Connect up to 5 Android phones to spread load and stay reliable at higher volume.

### Open Source

The whole stack is on GitHub: audit it, self-host it, and trust exactly what you run.

### Message Scheduling

Queue messages for a specific time or on a recurring schedule and let textbee send them.

How it works

## Live in under 5 minutes

Install the app to turn your Android device into an SMS gateway, then call the API from your own applications. No carrier contracts, no hardware.

![Diagram: your Android phone connects through the textbee cloud API to your web app, server, and code](https://textbee.dev/_next/image?url=%2Fimages%2Fgateway-diagram.png&w=3840&q=75)
1. 130 seconds
	### Download the Android app
	Install the free, open-source textbee app on any Android phone.
	[Get the app](https://textbee.dev/download)
2. 21 minute
	### Generate an API key
	Create a secure API key from your dashboard. Unlimited keys per account.
	[Open dashboard](https://app.textbee.dev/dashboard)
3. 31 minute
	### Scan the QR code
	Scan the code in the app (or paste the key) and enable the gateway.
4. 4Instant
	### Start sending
	Fire your first SMS from the dashboard or the API. You are live.
	[View API docs](https://textbee.dev/docs/sending-sms/sending-sms)

## Watch the demo

See how TextBee turns an Android phone into an SMS gateway in minutes.

![](https://www.youtube.com/watch?v=QNSJ8f411vY)

Developer Friendly

## Simple Integration in Minutes

Our REST API makes it easy to integrate SMS capabilities into any application. Just a few lines of code is all you need.

### Send an SMS message

Choose your preferred language

Endpoint: POST /send-sms

Rate limit: 60/min

```
import axios from 'axios'

const API_KEY = 'YOUR_API_KEY'
const DEVICE_ID = 'YOUR_DEVICE_ID'

const response = await axios.post(\`https://api.textbee.dev/api/v1/gateway/devices/${DEVICE_ID}/send-sms\`, {
  recipients: [ '+1234567890' ],
  message: 'Hello from textbee.dev!',
}, {
  headers: {
    'x-api-key': API_KEY,
  },
})

console.log(response.data)
```

Full API documentation is available at [textbee.dev/docs](https://textbee.dev/docs)

Simple Pricing

## Simple, transparent pricing

Flat pricing with no per-message fees. Plans that grow with you, cancel anytime. Save 17% with annual billing.

You're saving 17% with annual billing (2 months free)

### Frequently Asked Questions

Twilio gives you guaranteed carrier-grade throughput. If you're sending a million 2FA codes a day, use Twilio. If you're sending 500–50,000/mo and want to keep the money, use textbee.

Custom solutions

## Need more than the platform?

From self-hosting to bespoke integrations, our team helps you ship textbee.dev your way, and tackle development projects beyond it.

### Self-Hosting Setup

Get assistance deploying textbee.dev on your own infrastructure with secure configuration and optimization.

- Complete control
- Custom configuration

### Custom Integrations

Integrate textbee.dev seamlessly with your existing applications, APIs, and business workflows.

- Streamlined processes
- Data synchronization
- Automation

### Development Projects

Collaborate with our team on your software development needs beyond textbee.dev.

- Expert consultancy
- Tailored solutions
- Ongoing support

#### Ready to elevate your project?

Contact us to discuss your requirements and get a tailored solution.

Android App

## Download the textbee.dev App and Get Started in Minutes

Transform your Android device into a powerful SMS gateway with our easy-to-use application. Install, connect, and start sending messages programmatically.

Compatible with Android 7.0+ devices.

![textbee.dev Android SMS gateway app running on a phone](https://textbee.dev/_next/image?url=%2Fimages%2Fapp-mockup.png&w=1080&q=75)

Connected

Scan QR to download

[View setup instructions](https://textbee.dev/blog/textbee-dev-sms-gateway-quickstart)

## Your phone is already an SMS gateway. Switch it on.

Set up in minutes and send your first message for free. No credit card, no per-message fees, no carrier contracts.

Free tier forever No credit card required Open source