package hbrs.webengineering.servlet;

import de.pbrsystems.ais.Ship;
import de.pbrsystems.ais.ShipReceiver;

import javax.servlet.ServletException;
import javax.servlet.annotation.WebServlet;
import javax.servlet.http.HttpServlet;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;
import java.io.IOException;
import java.io.PrintWriter;
import java.util.List;
import java.util.ListIterator;

/**
 * Provides live ship data.
 */
@WebServlet(name = "ShipServlet", urlPatterns = {"/ships"})
public class ShipServlet extends HttpServlet {
    protected void doGet(HttpServletRequest request, HttpServletResponse response) throws ServletException, IOException {
        PrintWriter writer = response.getWriter(); // String buffer for JSON serialization

        List<Ship> results = ShipReceiver.loadShipsFromServer(); // Load data from server

        response.setContentType("application/json");

        writer.append("["); // JSON array start

        // Iterate over ship results with iterator in order to able to detect the last element
        ListIterator<Ship> shipIterator = results.listIterator();
        while (shipIterator.hasNext()) { // Serialize every ship
            Ship ship = shipIterator.next();

            writer.append("{"); // JSON object start
            writer.append("\"mmsi\":");
            writer.append(ship.getMmsi().toString());
            writer.append(",\"latitude\":");
            writer.append(ship.getLatitude().toString());
            writer.append(",\"longitude\":");
            writer.append(ship.getLongitude().toString());
            writer.append(",\"courseOverGround\":");
            writer.append(ship.getCourseOverGround().toString());
            writer.append("}");

            if (shipIterator.hasNext()) { // Not the last ship?
                writer.append(",");
            }
        }
        writer.append("]");
    }
}
