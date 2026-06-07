# Borrowing

ระบบจัดการการยืมหนังสือที่ใช้ Django ซึ่งช่วยให้ผู้ใช้สามารถจัดการและติดตามการยืมหนังสือได้อย่างมีประสิทธิภาพ

## 📋 คำอธิบายโปรเจกต์

Borrowing เป็นเว็บแอปพลิเคชันที่สร้างด้วย Django เพื่อช่วยในการจัดการคลังหนังสือหรือคอลเลกชันหนังสือส่วนบุคคล ผู้ใช้สามารถติดตามว่าหนังสือใดถูกยืมไป ใครยืมไป และจัดการกระบวนการยืมหนังสือได้อย่างมีประสิทธิภาพ

## 🛠️ เทคโนโลยีที่ใช้

- **Backend**: Python
- **Framework**: Django
- **Database**: SQLite (ค่าเริ่มต้น)
- **Version Control**: Git

## 📁 โครงสร้างโปรเจกต์

```
Borrowing/
├── Borrowing/          # การตั้งค่า Django project หลัก
├── books/              # Django app สำหรับจัดการหนังสือ
├── manage.py           # ยูทิลิตี้คำสั่งจัดการ Django
├── db.sqlite3          # ฐานข้อมูล SQLite
└── .gitignore          # กฎสำหรับ Git ignore
```

## 🚀 เริ่มต้นใช้งาน

### ข้อกำหนดเบื้องต้น

- Python 3.x
- pip (Python package manager)
- Virtual environment (แนะนำให้ใช้)

### วิธีติดตั้ง

1. **โคลนโปรเจกต์**
   ```bash
   git clone https://github.com/ManYaiMark/Borrowing.git
   cd Borrowing
   ```

2. **สร้างและเปิดใช้งาน virtual environment**
   ```bash
   # บน Windows
   python -m venv venv
   venv\Scripts\activate

   # บน macOS/Linux
   python3 -m venv venv
   source venv/bin/activate
   ```

3. **ติดตั้ง dependencies**
   ```bash
   pip install django
   ```

4. **รันการ migrate ฐานข้อมูล**
   ```bash
   python manage.py migrate
   ```

5. **เปิดเซิร์ฟเวอร์พัฒนา**
   ```bash
   python manage.py runserver
   ```

   แอปพลิเคชันจะเข้าถึงได้ที่ `http://127.0.0.1:8000/`

## 📝 ฟีเจอร์

- จัดการคลังหนังสือ
- ติดตามหนังสือที่ถูกยืม
- ประวัติการยืมหนังสือของผู้ใช้
- จัดการฐานข้อมูลผ่าน Django admin

## 🔧 คำสั่งจัดการ Django

คำสั่ง Django management ทั่วไปสำหรับโปรเจกต์นี้:

```bash
# สร้างผู้ดูแลระบบเพื่อเข้าถึง admin
python manage.py createsuperuser

# สร้าง app ใหม่
python manage.py startapp <app_name>

# สร้าง migrations
python manage.py makemigrations

# ใช้ migrations
python manage.py migrate

# เข้าสู่ Django shell
python manage.py shell
```

## 📚 แผงควบคุม Admin

เข้าถึง Django admin interface ที่ `/admin` หลังจากสร้างผู้ดูแลระบบ:

```bash
python manage.py createsuperuser
```

จากนั้นเข้าไปที่ `http://127.0.0.1:8000/admin/` และเข้าสู่ระบบด้วยข้อมูลประจำตัวของคุณ

## 📦 Dependencies

- Django

ดูไฟล์ `requirements.txt` (หากมี) สำหรับรายการ dependencies ที่ครบถ้วน

## 🤝 มีส่วนร่วมในโปรเจกต์

1. Fork โปรเจกต์
2. สร้าง branch ใหม่ (`git checkout -b feature/AmazingFeature`)
3. Commit การเปลี่ยนแปลง (`git commit -m 'Add some AmazingFeature'`)
4. Push ไปที่ branch (`git push origin feature/AmazingFeature`)
5. เปิด Pull Request

## 📄 ลิขสิทธิ์

โปรเจกต์นี้ยังไม่มีใบอนุญาต โปรดเพิ่มไฟล์ LICENSE หากคุณต้องการเปิดเผยซอร์สโค้ด

## ✉️ ติดต่อ

หากมีคำถามหรือข้อเสนอแนะ โปรดเปิด issue ในโปรเจกต์นี้

---

**อัปเดตครั้งล่าสุด**: มิถุนายน 2026
