from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User,auth
from .models import *
from django.contrib import messages
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from .models import Bookings
from .forms import BookingStatusForm
from .models import Bookings, Partner
# Create your views here.

def home_page(request):
  return render(request,'home.html')

def test(request):
  return render(request,'test.html')

def success(request):
  return render(request,'successfully.html')

def login_page(request):
    if request.method == 'POST':
        username = username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username = username,password = password)

        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, "invalid credentials!")
            return redirect('login_page')
        
    return render(request, 'login.html')
        
def register_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        # phonenumber = request.POST.get('phone')
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        
        # if not all([username, password, confirm_password, email, first_name, last_name]):
        #     messages.info(request, "All fields are required!")
        #     return redirect('register')

        if password != confirm_password:
            messages.info(request, "Passwords do not match!")
            return redirect('register_page')

        if User.objects.filter(username=username).exists():
            messages.info(request, "Username is already taken!")
            return redirect('register_page')

        if User.objects.filter(email=email).exists():
            messages.info(request, "Email is already taken!")
            return redirect('register_page')

       
        user = User.objects.create_user(
                username=username,
                password=password,
                email=email,
              
            )
        user.save()
        messages.success(request, "User registered successfully!")
        return redirect('login_page') 

    return render(request, 'register.html')


def logout_page(request):
    auth.logout(request)
    return redirect('/')

    #booking page

def booking_view(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        location = request.POST.get('location')
        
        # Extract all purposes, dates, times, and hours from the dynamic fields
        purpose = request.POST.get('purpose')
        date = request.POST.get('date')
        time= request.POST.get('time')
        hour= request.POST.get('hours')
        
        # Save each entry into the database
        # for i in range(len(purposes)):
        #     purpose = purposes[i]
        #     date = dates[i]
        #     time = times[i]
        #     hours = int(hours_list[i])

            
            # Create a new booking entry
        booking_obj=Bookings.objects.create(
                name=name,
                phone=phone,
                location=location,
                purpose=purpose,
                date=date,
                time=time,
                hours=hour,
            )
        booking_obj.save()

        messages.success(request, "Booked successfully!")
        return redirect('/view_bookings') 
    
    return render(request, 'booking.html')  # Render the booking form

def view_booking(request):
    if request.user.is_authenticated:
        # Fetch bookings for the logged-in user
        bookings = Bookings.objects.filter(name=request.user.username).order_by('id')
        return render(request, 'viewbooking.html', {'bookings': bookings})
    else:
        return redirect('login')


#admin update_booking_status
def update_booking_status(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == 'POST':
        form = BookingStatusForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            return redirect('success')
    else:
        form = BookingStatusForm(instance=booking)
    return render(request, 'update_status.html', {'form': form, 'booking': booking})

def partner_home(request):
    if request.method == 'POST':
        # Extract data from the POST request
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        adhaar = request.POST.get('adhaar')
        city = request.POST.get('city')


           # Create a new booking entry
        partner_obj=Partner.objects.create(
                name=name,
                phone=phone,
                password=password,
                adhaar=adhaar,
                city=city,
                
            )
        partner_obj.save()
        messages.success(request, "Booked successfully!")
        return redirect('/partner_message') 

    return render(request,'partnerHome.html')
    
    
def partner_login(request):
    if request.method == 'POST':
        phone = request.POST.get('phone')
        password = request.POST.get('password')

        partner_obj = None
        try:
            # Ensure the authenticate function exists and works correctly
            partner_obj = Partner.auth.authenticate(phone=phone, password=password)
        except Exception as e:
            messages.info(request, "An error occurred during authentication.")
            return redirect('/partner_login')

        if partner_obj is not None:
            Partner.auth.login(request, partner_obj)
            return redirect('partner_main')
        else:
            
            messages.info(request, "Invalid credentials!")
            return redirect('/partner_login')

    return render(request, 'partnerLogin.html')


def partner_main(request):
     return render(request,'partnerMain.html')

# View for admin to update booking status
def update_booking_status(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == 'POST':
        form = BookingStatusForm(request.POST, instance=booking)
        if form.is_valid():
            form.save()
            messages.success(request, "Booking status updated successfully!")
            return redirect('success')
    else:
        form = BookingStatusForm(instance=booking)
    return render(request, 'update_status.html', {'form': form, 'booking': booking})

# View for partners to see verified works
def partner_work_list(request):
    # if request.user.is_authenticated:
        works = Bookings.objects.filter(status='Verified')  # Only show verified works
        return render(request, 'partner_work_list.html', {'works': works})
    # else:
    #     return redirect('partner_login')

# View for partners to accept or reject works
def update_partner_status(request, booking_id):
    booking = get_object_or_404(Bookings, id=booking_id)
    if request.method == 'POST':
        action = request.POST.get('action')
        if action == 'accept':
            booking.partner_status = 'Accepted'
        elif action == 'reject':
            booking.partner_status = 'Rejected'
        booking.save()
        messages.success(request, "Partner's decision recorded successfully!")
        return redirect('partner_work_list')
    return render(request, 'update_partner_status.html', {'booking': booking})


def index(request):
     return render(request,'index.html')

def partner_message(request):
     return render(request,'partner_message.html')
