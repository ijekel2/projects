package com.personalitea.personalities;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * Created by nathanjekel on 1/30/18.
 */

@WebServlet(urlPatterns = "/delete-type.do")
public class DeletePersonalityTypeServlet extends HttpServlet {

    private PersonalityTypeService personalityTypeService = new PersonalityTypeService();

    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        personalityTypeService.deletePersonalityType(new PersonalityType(request.getParameter("personalityType")));
        response.sendRedirect("/types.do");
    }

}
