package com.personalitea.personalities;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;

/**
 * Created by nathanjekel on 2/13/18.
 */
@WebServlet(urlPatterns = "/add-type.do")

public class AddPersonalityTypeServlet {

    private PersonalityTypeService personalityTypeService = new PersonalityTypeService();

    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {

        String addedType = request.getParameter("personalityType");
        personalityTypeService.addPersonalityType(new PersonalityType(addedType));
        response.sendRedirect("/types.do");
    }
}
