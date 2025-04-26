
# Sober Indiana Free Rides Notifier

This project monitors the **Sober Ride Indiana** website for updates about free Uber and Lyft rides. When a new promotion is available, the system automatically sends a notification to a designated Slack channel.

---

## 📋 How It Works

- Scrapes the [Sober Ride Indiana](https://soberrideindiana.com/redeem) webpage.
- Checks if a new free ride promotion is available.
- Posts an update to a specified Slack channel using a webhook.
- Maintains a local `data.json` file to track the last notified promotion and avoid duplicate notifications.

---

## 🚀 Setup Instructions

1. **Clone the Repository**
   ```
   git clone https://github.com/harshasic/sober-ride-notifier.git
   cd sober-ride-notifier
   ```

2. **Install Dependencies**
   ```
   pip install beautifulsoup4 requests
   ```

3. **Configure Slack Webhook**
   - Replace the webhook URL inside the `postData` function (`https://hooks.slack.com/services/...`) with your own Slack incoming webhook URL.
   - You can create a Slack incoming webhook [here](https://api.slack.com/messaging/webhooks).

4. **Run the Script**
   ```
   python soberIndiana.py
   ```

---

## 🛠 Project Structure

| File | Purpose |
| :--- | :------ |
| `soberIndiana.py` | Main script to scrape ride info and notify via Slack |
| `data.json` | Stores the last notified ride to prevent duplicate alerts |

---

## ⚙️ How to Automate

You can automate this script to run periodically (e.g., every hour) using cron jobs (Linux/Mac) or Task Scheduler (Windows).

Example (Linux):
```
0 * * * * /usr/bin/python3 /path/to/soberIndiana.py
```
This will run the script every hour.

---

## 📌 Notes

- Keep your Slack webhook URL secure.
- Ensure you have permission to scrape the Sober Ride Indiana website. This project is for educational and personal use only.
- The website structure might change over time. If the script stops working, update the scraping logic inside the `findNextSoberRide` function.

---

## 📄 License

This project is open-source and available under the [MIT License](LICENSE).

---

## 🙌 Acknowledgments

- [BeautifulSoup](https://www.crummy.com/software/BeautifulSoup/) - For HTML parsing
- [Sober Ride Indiana](https://soberrideindiana.com/) - Free ride service initiative

