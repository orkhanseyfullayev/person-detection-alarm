# Person Detection Alarm System

A Python-based real-time person detection and alert system utilizing **YOLOv8** for object detection and **SMTP** for email notifications. This project is designed to detect the presence of a person through a live camera feed and send an email alert with an image attachment when a person is detected.

---

## Features
- **Real-time person detection** using the YOLOv8 model.
- **Email notifications** with an attached image when a person is detected.
- Customizable alert timing to prevent multiple notifications.
- Easily adaptable for other object detection use cases.

---

## Requirements

Ensure you have the following installed:
- Python 3.7+
- OpenCV
- UltraLytics YOLO
- SMTP-compatible email account (e.g., Gmail with App Passwords enabled)

Install required Python packages:
```bash
pip install ultralytics opencv-python
```

---

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/person-detection-alarm.git
   cd person-detection-alarm
   ```

2. **Configure your email credentials:**
   Open the `mail_send` function in `main.py` and replace:
   - `sender_email` → Your email address.
   - `password` → Your email account's App Password.
   - `send_to` → Recipient email address.

3. **Run the program:**
   ```bash
   python main.py
   ```

4. **Live Detection:**
   The camera feed will display bounding boxes for detected persons. If a person is detected for a certain duration, an email alert will be sent with the current frame attached.

---

## File Structure

```
📂 person-detection-alarm
├── main.py           # Main script for person detection and email alerts
├── README.md         # Project documentation
```

---

## Customization

- **Detection Threshold:**
  Modify the `score` threshold in the `main.py` file to adjust the sensitivity of person detection.
  ```python
  if score < 0.5:
      continue
  ```

- **Alert Interval:**
  Change the `time_for_alarm` variable to set the delay between consecutive email alerts:
  ```python
  time_for_alarm = 5  # in seconds
  ```

---

## Future Improvements
- Adding support for multiple object detection.
- Integrating cloud storage for image attachments.
- Enhancing alert mechanisms with SMS or push notifications.

---

## License
This project is licensed under the [MIT License](LICENSE). Feel free to use, modify, and share it.

---

## Author
Developed by **[Orkhan Seyfullayev](https://github.com/orkhanseyfullayev)**. For queries, reach out via email or GitHub.
