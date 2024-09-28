from django.shortcuts import render,redirect
from .forms import CustomUserCreationForm
from django.contrib.auth import login,authenticate

# Create your views here.
def signup_view(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            # ล็อกอินอัตโนมัติหลังจากสมัครเสร็จ
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            if user is not None:
                login(request, user)
                return redirect('home')  # เปลี่ยนเป็น URL ที่ต้องการ redirect หลังจากสมัครเสร็จ
        else:
            print(form.errors)  # เพิ่มการแสดงผลข้อผิดพลาดใน console เพื่อตรวจสอบ
    else:
        form = CustomUserCreationForm()

    return render(request, 'users/signup.html', {'form': form})

# def signup_view(request):
#   if request.method == 'POST':
#     form = CustomUserCreationForm(request.POST)
#     if  form.is_valid():
#       user = form.save()
#       login(request,user)
#       print('suces')
#       return redirect('home')
#   else:
#     print('no suces')
#     form = CustomUserCreationForm()
#   print('run signup')
#   return render(request,'users/signup.html',{'form':form})

def login_view(request):
  if request.method == 'POST':
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        user = authenticate(request, username=username, password=password)
        if user is not None:
          login(request, user)
          return redirect('home')
        else:
          return render(request, 'users/login.html', {'error': 'Invalid credentials'})
    else:
        return render(request, 'users/login.html', {'error': 'Please provide both username and password'})
    
  return render(request,'users/login.html')


