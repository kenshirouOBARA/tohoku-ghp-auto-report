import os, smtplib, datetime as dt
from email.mime.text import MIMEText

def main() -> None:
    # -------------------------------
    # 1) 本文を作る（今回はテスト用の固定文）
    # -------------------------------
    today = dt.date.today().isoformat()
    body = f"""
    <h2>GHP 自動レポート（テスト送信）</h2>
    <p>{today} 時点でのデータはまだありません。</p>
    """

    # -------------------------------
    # 2) メールを組み立てる
    # -------------------------------
    msg = MIMEText(body, "html", "utf-8")
    msg["Subject"] = f"【月次GHPレポート】テスト送信 {today}"
    msg["From"]    = os.environ["GMAIL_USER"]          # Secrets に登録した送信元
    msg["To"]      = "kenshiro_obara@yanmar.com"       # <-- 届けたいアドレス

    # -------------------------------
    # 3) Gmail 経由で送信
    # -------------------------------
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as smtp:
        smtp.login(os.environ["GMAIL_USER"], os.environ["GMAIL_PASS"])
        smtp.send_message(msg)
        print("Message sent to", msg["To"])

if __name__ == "__main__":
    main()
