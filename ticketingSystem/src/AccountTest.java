import org.junit.jupiter.api.Test;

import java.io.File;
import java.io.FileNotFoundException;
import java.util.Scanner;

import static org.junit.jupiter.api.Assertions.*;

public class AccountTest extends Backend{

    @Test
    public void shouldGetAccountName(){
        String name = "billw           BS 000300.00";
        String nameTrue = "billw";
        accounts.add(name);
        Backend.getAccountNames();
        assertTrue(Backend.users.contains(nameTrue));
    }

    @Test
    public void deleteAccountTest(){
        String transaction = "02 ryanw           BS 000300.00";
        Backend.deleteUser(transaction);
        Backend.getAccountNames();
        assertFalse(Backend.users.contains("ryanw"));
    }

    @Test
    public void addCreditTest() throws FileNotFoundException {
        String transaction = "06 admin           AA 000200.00";
        Backend.getAccountNames();
        Backend.addCredit(transaction);
        String account = "";
        String expected = "admin           AA 000300.00";
        try{
            File accounts = new File(System.getProperty("user.dir") + "/newAccounts.txt");
            Scanner scan = new Scanner(accounts);
            while (scan.hasNextLine()) {
                if(scan.nextLine().contains(expected)){
                    account = scan.nextLine();
                }
            }
            assertEquals(expected, account);
            scan.close();
        } catch (Exception e) {
            e.printStackTrace();
        }
    }



}
