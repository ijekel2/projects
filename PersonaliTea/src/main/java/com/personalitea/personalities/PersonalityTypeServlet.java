package com.personalitea.personalities;

import com.personalitea.login.LoginService;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * Created by nathanjekel on 1/30/18.
 */

@WebServlet(urlPatterns = "/types.do")
public class PersonalityTypeServlet extends HttpServlet {

    private PersonalityTypeService personalityTypeService = new PersonalityTypeService();

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        request.setAttribute("personalityTypeList", personalityTypeService.getPersonalityTypeList());
        request.getRequestDispatcher("WEB-INF/views/personality-types.jsp").forward(request, response);

    }




}
