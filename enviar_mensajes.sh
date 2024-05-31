#!/bin/bash

curl -i -X POST \
  "https://graph.facebook.com/v19.0/273227425884274/messages" \
    -H 'Authorization: Bearer EAAQ8M5422F0BO9gjSYC3LR5pFK7YEW5dSmcjMDGNJKuH0jIGKgKuK6mXNvr7N42aZCzqwjaZCQsbJbyueNZCk1TZBDh5LyLi7RTiV9sZCLmd0uSZCGilGVS5H9FnN6MY8J28CQ3kkZCVW4hUcF3eGTNG8GnxoRumrPy0fcmJUqRbPRnG0ZAXKynQcZCLY94H9tibZA7yT5s1ZBhRIFAt0kdFlwZD' \
	-H 'Content-Type: application/json' \
	-d '{"messaging_product": "whatsapp", "to": "34642571533", "type": "template", "template": {"name": "hello_world", "language": {"code": "en_US"}}}'

