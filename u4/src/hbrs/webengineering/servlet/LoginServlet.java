package hbrs.webengineering.servlet;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;
import java.util.HashSet;

@WebServlet(name = "LoginServlet", urlPatterns = {"/login"})
public class LoginServlet extends HttpServlet {
    protected void doPost(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        HttpSession session;

        if (request.getParameter("pwd").equals("secret!")) {
            session = request.getSession(true); // Get session or create it if it doesn't exist
            session.setAttribute("authenticated", true);
            response.sendRedirect("tracker.html");
        } else {
            response.sendRedirect("login.html");
        }
    }
}
