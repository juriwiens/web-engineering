package hbrs.webengineering.filter;

import javax.servlet.*;
import javax.servlet.annotation.WebFilter;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import javax.servlet.http.HttpSession;
import java.io.IOException;

@WebFilter(filterName = "LoginFilter", urlPatterns = "/*")
public class LoginFilter implements Filter {
    public void destroy() {
    }

    public void doFilter(ServletRequest req, ServletResponse resp, FilterChain chain) throws ServletException, IOException {
        Boolean authenticated = null; // Authenticated session attribute

        // Cast resquest and response
        HttpServletRequest httpReq = (HttpServletRequest) req;
        HttpServletResponse httpResp = (HttpServletResponse) resp;

        // Exclude requests to login.html and LoginServlet to avoid a redirect loop
        if (httpReq.getRequestURI().endsWith("login.html") || httpReq.getRequestURI().endsWith("/login")) {
            chain.doFilter(req, resp);
            return;
        }

        HttpSession session = httpReq.getSession(false); // Try to get session
        if (session != null) {
            authenticated = (Boolean) session.getAttribute("authenticated");
        }

        if (authenticated == null || !authenticated) {
            httpResp.sendRedirect("login.html"); // Unauthenticated, so redirect to login page
        } else {
            chain.doFilter(req, resp); // Go on
        }

    }

    public void init(FilterConfig config) throws ServletException {

    }

}
