import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;
import java.sql.ResultSet;
import java.sql.SQLException;
import java.util.Scanner;

public class DatabaseOperations {

    private static final String JDBC_URL = "jdbc:mysql://your_mysql_host:3306/your_database_name";
    private static final String USER = "your_mysql_user";
    private static final String PASSWORD = "your_mysql_password";

    public static void main(String[] args) {
        try (Connection connection = DriverManager.getConnection(JDBC_URL, USER, PASSWORD)) {
            Scanner scanner = new Scanner(System.in);

            while (true) {
                System.out.println("\nDatabase Navigation Operations:");
                System.out.println("1. Add Record");
                System.out.println("2. Delete Record");
                System.out.println("3. Edit Record");
                System.out.println("4. Exit");

                System.out.print("Enter your choice (1/2/3/4): ");
                String choice = scanner.nextLine();

                switch (choice) {
                    case "1":
                        addRecord(connection);
                        break;
                    case "2":
                        deleteRecord(connection);
                        break;
                    case "3":
                        editRecord(connection);
                        break;
                    case "4":
                        return;
                    default:
                        System.out.println("Invalid choice. Please enter a valid option.");
                }
            }
        } catch (SQLException e) {
            e.printStackTrace();
        }
    }

    private static void addRecord(Connection connection) throws SQLException {
        try (PreparedStatement preparedStatement =
                     connection.prepareStatement("INSERT INTO your_table_name (name, age) VALUES (?, ?)")) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter name: ");
            String name = scanner.nextLine();

            System.out.print("Enter age: ");
            int age = scanner.nextInt();

            preparedStatement.setString(1, name);
            preparedStatement.setInt(2, age);

            preparedStatement.executeUpdate();
            System.out.println("Record added successfully!");
        }
    }

    private static void deleteRecord(Connection connection) throws SQLException {
        try (PreparedStatement preparedStatement =
                     connection.prepareStatement("DELETE FROM your_table_name WHERE id = ?")) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter the ID of the record to delete: ");
            int recordId = scanner.nextInt();

            preparedStatement.setInt(1, recordId);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Record deleted successfully!");
            } else {
                System.out.println("No record found with the specified ID.");
            }
        }
    }

    private static void editRecord(Connection connection) throws SQLException {
        try (PreparedStatement preparedStatement =
                     connection.prepareStatement("UPDATE your_table_name SET age = ? WHERE id = ?")) {
            Scanner scanner = new Scanner(System.in);

            System.out.print("Enter the ID of the record to edit: ");
            int recordId = scanner.nextInt();

            System.out.print("Enter the new age: ");
            int newAge = scanner.nextInt();

            preparedStatement.setInt(1, newAge);
            preparedStatement.setInt(2, recordId);

            int rowsAffected = preparedStatement.executeUpdate();
            if (rowsAffected > 0) {
                System.out.println("Record edited successfully!");
            } else {
                System.out.println("No record found with the specified ID.");
            }
        }
    }
}
