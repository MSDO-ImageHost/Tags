from jose import jwt
import time

#It decodes the token and makes sure that the issuer is what we expect and that it has not expired
def verify(token):
    decoded = jwt.decode(token, "secret", algorithms=['HS256'])
    millis = int(round(time.time() * 1000))
    if (decoded["iss"] == "ImageHost.sdu.dk" and decoded["exp"] < millis):
        return decoded
    else:
        return None

if __name__ == "__main__":
    old_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiIxIiwicm9sZSI6ImFkbWluIiwiaXNzIjoiSW1hZ2VIb3N0LnNkdS5kayIsImV4cCI6MTYwNjkyODMwMywiaWF0IjoxNjA2OTI0NzAzfQ.TC5wpxA20V-zhorK0EVIQbjIZdPX2Uy-PLrw7mYIeng"
    token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1Iiwicm9sZSI6InVzZXIiLCJpc3MiOiJJbWFnZUhvc3Quc2R1LmRrIiwiZXhwIjoxNjM4NTYwNzEzLCJpYXQiOjE2MDcwMjQ3MTN9._AErjVtL5cs72HNi55LMhDi2VLhH-VDKr09_7gBGwDg"
    new_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJzdWIiOiI1Iiwicm9sZSI6MCwiaXNzIjoiSW1hZ2VIb3N0LnNkdS5kayIsImV4cCI6MTYzODU2MDcxMywiaWF0IjoxNjA3MDI0NzEzfQ.BEd5MV1_8Vukwk-zX3cNKrXKF_ZseIBmahYt7-PopB8"
    decoded_token = verify(new_token)
    print(decoded_token)
