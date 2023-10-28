import java.io.BufferedReader;
import java.io.InputStreamReader;

public class PythonIntegration {
    public static String runPythonScript() {
        try {
            Process process = Runtime.getRuntime().exec("C:/Users/haris/AppData/Local/Microsoft/WindowsApps/python3.10.exe c:/Users/haris/Desktop/SnapAttendance/recognize.py");
            BufferedReader reader = new BufferedReader(new InputStreamReader(process.getInputStream()));
            StringBuilder builder = new StringBuilder();
            String line;

            while ((line = reader.readLine()) != null) {
                builder.append(line);
            }

            return builder.toString();
        } catch (Exception e) {
            e.printStackTrace();
            return "Error: " + e.getMessage();
        }

    }

    public static void main(String[] args) {
        String recognitionResult = PythonIntegration.runPythonScript();
        System.out.println(recognitionResult);
    }
}


