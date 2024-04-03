package com.example.javalogin;

import jakarta.servlet.*;
import jakarta.servlet.ServletException;
import jakarta.servlet.annotation.WebServlet;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import java.io.*;

@WebServlet(name = "JavaLogin", value = "/LoginServlet")
public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {

        String username = request.getParameter("username");
        String password = request.getParameter("password");

        // Kiểm tra username và password
        if(username.equals("admin") && password.equals("admin123")) {
            // Đăng nhập thành công
            response.sendRedirect("success.jsp");
            return;
        } else {
            // Đăng nhập thất bại
            response.sendRedirect("failure.jsp");
            return;
        }
    }
}