from django.shortcuts import render, redirect
from django.contrib import messages
from django.db import connection
from decouple import config
import bcrypt

def settings(request):
    auth_token = request.COOKIES.get(config('COOKIE_KEY_1'))
    role = request.COOKIES.get(config('COOKIE_KEY_2'))

    if not auth_token or not role:
        return redirect('/login/')

    if request.method == 'POST':
        current_password = request.POST.get("current_password")
        new_password = request.POST.get("new_password")
        confirm_password = request.POST.get("confirm_password")

        if not current_password or not new_password or not confirm_password:
            messages.error(request, "All fields are required.")
            return render(request, 'settings.html',{ 'role': role })

        if new_password != confirm_password:
            messages.error(request, "New passwords do not match.")
            return render(request, 'settings.html',{ 'role': role })

        valid_roles = {
            "recruiter": "recruiter",
            "job_seeker": "job_seeker",
        }

        table_name = valid_roles.get(role)
        if not table_name:
            messages.error(request, "Invalid user role.")
            return render(request, 'settings.html',{ 'role': role })

        with connection.cursor() as cursor:
            query = f"SELECT password FROM {table_name} WHERE email = %s"
            cursor.execute(query, (auth_token,))
            user_data = cursor.fetchone()

            if not user_data:
                messages.error(request, "User not found.")
                return redirect('/login/')

            hashed_current_password = user_data[0]

            if not bcrypt.checkpw(current_password.encode('utf-8'), hashed_current_password.encode('utf-8')):
                messages.error(request, "Current password is incorrect.")
                return render(request, 'settings.html',{ 'role': role })

            hashed_new_password = bcrypt.hashpw(new_password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
            update_query = f"UPDATE {table_name} SET password = %s WHERE email = %s"
            cursor.execute(update_query, (hashed_new_password, auth_token))
            connection.commit()

        messages.success(request, "Password updated successfully.")
        response = redirect('/settings')
        # response.delete_cookie(config('COOKIE_KEY_1'))
        # response.delete_cookie(config('COOKIE_KEY_2'))
        return response

    return render(request, 'settings.html',{ 'role': role })

