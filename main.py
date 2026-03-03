from fastapi import FastAPI, Query
from pydantic import BaseModel
from jose import jwt
from datetime import datetime, timedelta
from fastapi.middleware.cors import CORSMiddleware


# Secret key for JWT (in production, keep it secret!)
SECRET_KEY = "supersecretkey"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 1
REFRESH_TOKEN_EXPIRE_DAYS = 7

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Allows all origins
    allow_credentials=True,
    allow_methods=["*"],  # Allows all methods (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Allows all headers
)

# Dummy user database


class LoginRequest(BaseModel):
    email: str
    password: str

class TokenResponse(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"

class StudentListResponse(BaseModel):
    marked:int
    total:int
    students:list

def create_access_token(data: dict, expires_delta: timedelta):
    to_encode = data.copy()
    expire = datetime.now() + expires_delta
    to_encode.update({"exp": expire})
    return jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)

@app.get("/")
def root():
    return {"message": "FastAPI Docker app running on Vercel!"}

@app.post("/login", response_model=TokenResponse)
def login(request: LoginRequest):
    email = request.email
    password = request.password


    access_token = create_access_token(
        {"sub": email},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    refresh_token = create_access_token(
        {"sub": email},
        expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    )

    return TokenResponse(access_token=access_token, refresh_token=refresh_token)


@app.get("/studentList" , response_model=StudentListResponse)
def studentList(date: datetime = Query(...)):

    stud = [
        {"name": "John Doe aklfj  lkjaf jkldajf klajfjdklj ojdfljajfihi", "enrollment": "ENR001" , "status" : "P"},
        {"name": "Jane Smith", "enrollment": "ENR002" , "status" : "A"},
        {"name": "John Doe", "enrollment": "ENR003" , "status" : "L"},
        {"name": "Jane Smith", "enrollment": "ENR004" , "status" : "N"},
        {"name": "John Doe", "enrollment": "ENR005" , "status" : "N"},
        {"name": "Jane Smith", "enrollment": "ENR006" , "status" : "P"},
        {"name": "John Doe", "enrollment": "ENR007" , "status" : "P"},
        {"name": "Jane Smith", "enrollment": "ENR008" , "status" : "A"},
        {"name": "John Doe", "enrollment": "ENR009" , "status" : "L"},
        {"name": "Jane Smith", "enrollment": "ENR010" , "status" : "P"},
        {"name": "John Doe", "enrollment": "ENR011" , "status" : "A"},
        {"name": "Jane Smith", "enrollment": "ENR012" , "status" : "L"},
        {"name": "John Doe", "enrollment": "ENR013" , "status" : "P"},
        {"name": "Jane Smith", "enrollment": "ENR014" , "status" : "N"}
    ]


    return StudentListResponse(marked = 8,total=30 , students=stud)

@app.get("/studentFee" , response_model=StudentListResponse)
def studentFee():

    stud = [
        {"name": "John Doe dkhalfkdaf  adjflkja  oajdfklj ", "enrollment": "ENR001" , "fee_submitted" : False , "contact" : "+91 234342424"},
        {"name": "Jane Smith", "enrollment": "ENR002" , "fee_submitted" : False , "contact" : "+91 234342424"},
        {"name": "John Doe", "enrollment": "ENR003" , "fee_submitted" : True , "contact" : "+91 234342424"},
        {"name": "Jane Smith", "enrollment": "ENR004" , "fee_submitted" : False ,"contact" : "+91 234342424"},
        {"name": "John Doe", "enrollment": "ENR005" , "fee_submitted" : True , "contact" : "+91 234342424"},
        {"name": "Jane Smith", "enrollment": "ENR006" , "fee_submitted" : False , "contact" : "+91 234342424"},
        {"name": "John Doe", "enrollment": "ENR007" , "fee_submitted" : True, "contact" : "+91 234342424"},
        {"name": "Jane Smith", "enrollment": "ENR008" , "fee_submitted" : False , "contact" : "+91 234342424"},
        {"name": "John Doe", "enrollment": "ENR009" , "fee_submitted" : True, "contact" : "+91 234342424"},
        {"name": "Jane Smith", "enrollment": "ENR010" , "fee_submitted" : False , "contact" : "+91 234342424"},
        {"name": "John Doe", "enrollment": "ENR011" , "fee_submitted" : True , "contact" : "+91 234342424"},
        {"name": "Jane Smith", "enrollment": "ENR012" , "fee_submitted" : False , "contact" : "+91 234342424"},
        {"name": "John Doe", "enrollment": "ENR013" , "fee_submitted" : True , "contact" : "+91 234342424"},
        {"name": "Jane Smith", "enrollment": "ENR014" , "fee_submitted" : False , "contact" : "+91 234342424"}
    ]


    return StudentListResponse(marked = 8 , total=30 , students=stud)

class NotifyFeeRequest(BaseModel):
    enrollment:str
@app.post("/notifyFee" , response_model=TokenResponse)
def notifyFee(request: NotifyFeeRequest):
    print(request.enrollment)
    return TokenResponse(access_token="access_token", refresh_token="refresh_token")


@app.get("/notifyFeeToAll" , response_model=TokenResponse)
def notifyFeeToAll():
    print("notified")
    return TokenResponse(access_token="access_token", refresh_token="refresh_token")


class submitAttendace(BaseModel):
    date:datetime
    attendance_data:list
import time
@app.post("/submitAttendance", response_model=TokenResponse)
def login(request: submitAttendace):
    print(request.attendance_data)
    time.sleep(5)
    access_token = create_access_token(
        {"sub": "email"},
        expires_delta=timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    )
    refresh_token = create_access_token(
        {"sub": "email"},
        expires_delta=timedelta(days=REFRESH_TOKEN_EXPIRE_DAYS)
    )

    return TokenResponse(access_token=access_token, refresh_token=refresh_token)
