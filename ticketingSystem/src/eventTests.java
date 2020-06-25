import org.junit.jupiter.api.Test;
import static org.junit.jupiter.api.Assertions.assertTrue;


public class eventTests{

    Backend backend = new Backend();

    @Test
    public void shouldGetEventName(){
        String name = "billy idol         admin           100 001.00";
        String nameTrue = "billy idol";
        backend.tickets.add(name);
        backend.getEventNames();
        assertTrue(backend.eventNames.contains(nameTrue));
    }


}
