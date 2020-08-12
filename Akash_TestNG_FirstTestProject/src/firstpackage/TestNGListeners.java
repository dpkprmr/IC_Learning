package firstpackage;

import java.io.File;
import java.io.IOException;

import org.apache.commons.io.FileUtils;
import org.openqa.selenium.OutputType;
import org.openqa.selenium.TakesScreenshot;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.chrome.ChromeDriver;
import org.testng.ITestContext;
import org.testng.ITestListener;
import org.testng.ITestResult;

public class TestNGListeners implements ITestListener {
	
	String driverPath = "D:\\ChromeDriver\\chromedriver_win32\\chromedriver.exe";
	public WebDriver driver;
	

	@Override
	public void onFinish(ITestContext Result) {
		System.out.println("TestCase is Finished"+ Result.getName());
		
	}

	@Override
	public void onStart(ITestContext Result) {
		System.out.println("TestCase is Started"+ Result.getName());
		
	}

	@Override
	public void onTestFailedButWithinSuccessPercentage(ITestResult Result) {
		System.out.println("TestCase is Fail with Success"+ Result.getName());
		
	}

	@Override
	public void onTestFailure(ITestResult Result) {
	
		
		System.out.println("TestCase is Failed"+ Result.getName());
		
	}

	@Override
	public void onTestSkipped(ITestResult Result) {
		System.out.println("TestCase is Skipped"+ Result.getName());
		
	}

	@Override
	public void onTestStart(ITestResult Result) {
		System.out.println("TestCase is STarted"+ Result.getName());
		
		
	}

	@Override
	public void onTestSuccess(ITestResult Result) {
		
		/*try {
		TakesScreenshot ts=(TakesScreenshot)driver;
		File source= 	ts.getScreenshotAs(OutputType.FILE);
		File DestFile = new File("./Screenshots/Login.png");
		FileUtils.copyFile(source, DestFile);
		} catch (IOException e) {
			e.printStackTrace();
		}*/
		System.out.println("TestCase is successfull"+ Result.getName());
		
		
	}

}
