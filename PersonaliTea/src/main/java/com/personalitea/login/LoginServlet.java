package com.personalitea.login;

import com.personalitea.personalities.PersonalityTypeService;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * Created by nathanjekel on 1/30/18.
 */

@WebServlet(urlPatterns = "/login.do")
public class LoginServlet extends HttpServlet {

    private LoginService loginService = new LoginService();
    private PersonalityTypeService personalityTypeService = new PersonalityTypeService();

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        request.setAttribute("username", request.getParameter("username"));
        request.setAttribute("password", request.getParameter("password"));


        request.getRequestDispatcher("WEB-INF/views/login.jsp").forward(request, response);

    }

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        String username = request.getParameter("username");
        String password = request.getParameter("password");

        boolean isValidUser = loginService.isValidUser(username, password);

        if(isValidUser) {
            request.getSession().setAttribute("username", username);
            response.sendRedirect("/types.do");
        } else {
            request.setAttribute("errorMessage", "Username or password is incorrect!");
            request.getRequestDispatcher("WEB-INF/views/login.jsp").forward(request, response);
        }
    }

}
