readme_content = """
# SENTIMENT ANALYSIS API USING FASTAPI

## 1. Thông tin sinh viên
- Họ tên: Đỗ Phước Thiện
- MSSV: 24120139
- Môn học: Tư duy tính toán

---

## 2. Mô hình sử dụng
- Tên mô hình: distilbert-base-uncased-finetuned-sst-2-english
- Nền tảng: Hugging Face
- Link: https://huggingface.co/distilbert-base-uncased-finetuned-sst-2-english

---

## 3. Mô tả hệ thống
Hệ thống xây dựng một Web API sử dụng FastAPI để phân tích cảm xúc văn bản (Sentiment Analysis).

Người dùng nhập một câu tiếng Anh, hệ thống sẽ trả về:
- POSITIVE (tích cực)
- NEGATIVE (tiêu cực)

---

## 4. Cài đặt

Cài thư viện:
pip install -r requirements.txt

---

## 5. Chạy chương trình

uvicorn main:app --reload

Sau đó mở:
http://127.0.0.1:8000/docs

---

## 6. API

### GET /
Trả về thông tin hệ thống

Response:
{
  "message": "Sentiment Analysis API"
}

---

### GET /health
Kiểm tra trạng thái hệ thống

Response:
{
  "status": "ok"
}

---

### POST /predict

Request:
{
  "text": "I love this product"
}

Response:
{
  "result": [
    {
      "label": "POSITIVE",
      "score": 0.99
    }
  ]
}

---

## 7. Kiểm thử

Cách 1: Mở trình duyệt
http://127.0.0.1:8000/docs

Cách 2: Chạy file test
python test_api.py

---

## 8. Xử lý lỗi

- Thiếu dữ liệu đầu vào → lỗi 400
- Sai định dạng → lỗi 400
- Lỗi hệ thống → lỗi 500

---

## 9. Video demo
Dán link video tại đây

---
