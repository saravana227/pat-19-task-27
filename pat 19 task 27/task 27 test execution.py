import pytest
import datetime

@pytest.mark.parametrize("username, password", [("user1", "pass1"), ("user2", "pass2"), ("user3", "pass3"), ("user4", "pass4"), ("user5", "pass5")])
def test_login(username, password):
    driver = webdriver.Firefox()
    login_page = LoginPage(driver)

    # Get current date and time
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")

    # Open the Excel file
    wb = openpyxl.load_workbook("test_results.xlsx")
    ws = wb.active

    try:
        login_page.login(username, password)
        # Add test data and result to the Excel file
        test_data = [ws.max_row, username, password, current_date, current_time, "TesterName", "Pass"]
        ws.append(test_data)
    except Exception as e:
        # If login fails, add test data and result to the Excel file
        test_data = [ws.max_row, username, password, current_date, current_time, "TesterName", "Fail"]
        ws.append(test_data)
    finally:
        # Save the changes to the Excel file
        wb.save("test_results.xlsx")
        driver.quit()