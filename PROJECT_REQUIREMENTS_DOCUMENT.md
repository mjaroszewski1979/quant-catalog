## Project Requirements Document for Digital Gold

### Unit Tests

#### Index View Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The index view must handle GET requests correctly. | When a GET request is made to the index URL. | The response should have a status code of 200 and use the index.html template. The response must contain the text 'Quant Catalog Home'. The context should include the test strategy. | test_index_get

#### CAGR Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The CAGR page must handle GET requests correctly. | When a GET request is made to the CAGR URL. | The response should have a status code of 200 and use the cagr.html template. The response must contain the text 'Quant Catalog CAGR'. | test_cagr_get

#### Sharpe Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Sharpe page must handle GET requests correctly. | When a GET request is made to the Sharpe URL. | The response should have a status code of 200 and use the sharpe.html template. The response must contain the text 'Quant Catalog Sharpe'. | test_sharpe_get

#### Long Only Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Long Only page must handle GET requests correctly. | When a GET request is made to the Long Only URL. | The response should have a status code of 200 and use the long.html template. The response must contain the text 'Quant Catalog Long Only'. | test_long_get

#### Search Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Search page must handle GET requests correctly. | When a GET request is made to the Search URL. | The response should have a status code of 200 and use the search.html template. The response must contain the text 'Quant Catalog Search'. | test_search_get
The search functionality must process query parameters correctly. | When a GET request is made to the Search URL with a query parameter. | The response should correctly reflect the query in the context. The context should include the query, the corresponding market, and the relevant strategy. | test_search_query

#### Signup Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Signup page must handle GET requests correctly. | When a GET request is made to the Signup URL. | The response should have a status code of 200 and use the signup.html template. The response must contain the text 'Quant Catalog Signup'. | test_signup_get
The Signup page must handle POST requests correctly to create a new user. | When a POST request is made to the Signup URL with user registration data. The response should redirect to the Login page upon successful signup. | The response must contain the text 'Quant Catalog Login'. | test_signup_post

#### Login Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Login page must handle GET requests correctly. | When a GET request is made to the Login URL. | The response should have a status code of 200 and use the login.html template. The response must contain the text 'Quant Catalog Login'. | test_login_get

#### Logout Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Logout URL must resolve to the correct view. | When a GET request is made to the Logout URL. | The response should direct the user to the appropriate post-logout page. | test_logout_url_is_resolved

#### Create Strategy Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Create Strategy page must handle GET requests correctly. | When a GET request is made to the Create Strategy URL. | The response should have a status code of 200 and use the strategies_create.html template. The response must contain the text 'Quant Catalog Create Strategy'. | test_strategies_create_get
The Create Strategy page must handle POST requests to create a new strategy. | When a POST request is made to the Create Strategy URL with strategy creation data. | The response should have the correct template and status code, reflecting the creation of a strategy. The response should contain the text 'Quant Catalog Create Strategy' | test_strategies_create_post

#### Update Strategy Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Update Strategy page must handle GET requests correctly. | When a GET request is made to the Update Strategy URL with a strategy slug. | The response should have a status code of 200 and use the strategies_update.html template. The response must contain the text 'Quant Catalog Update Strategy'. | test_strategies_update_get
The Update Strategy page must handle POST requests to update an existing strategy. | When a POST request is made to the Update Strategy URL with updated strategy data. | The response should have the correct template and status code, reflecting the update of the strategy. The response should contain the text 'Quant Catalog Update Strategy'. | test_strategies_update_post

#### Strategy Detail Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Strategy Detail page must handle GET requests correctly. | When a GET request is made to the Strategy Detail URL with a strategy slug. | The response should have a status code of 200 and use the strategy.html template. The response must contain the text 'Quant Catalog ' followed by the strategy title. | test_strategy_detail_get

#### Delete Strategy Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The Delete Strategy page must handle GET requests correctly. | When a GET request is made to the Delete Strategy URL with a strategy slug. | The response should have a status code of 200 and use the strategies_delete.html template if the user is in the 'quant' group. The response must contain the text 'Quant Catalog Delete Strategy'. | test_strategies_delete_user_in_group
Users not in the 'quant' group should be redirected on attempting to access the Delete Strategy page. | When a GET request is made to the Delete Strategy URL by a user not in the 'quant' group. | The response should redirect to the login page. | test_strategies_delete_user_not_in_group

### Selenium Tests

#### Index Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The index page must display the correct title. | When the index page is loaded. | The page title should be 'Quant Catalog Home'. | is_title_matches
The index page must display the correct heading. | When the index page is loaded. | The heading should be 'Hi, I’m Your Trading Mentor'. | is_index_heading_displayed_correctly
The signup link must navigate to the signup page correctly. | When the signup link on the index page is clicked. | The page title should change to 'Quant Catalog Signup'. | is_signup_link_works
The logo link must navigate back to the index page correctly. | When the logo link on the index page is clicked. | The page title should change to 'Quant Catalog Home'. | is_logo_link_works
The login link must navigate to the login page correctly. | When the login link on the index page is clicked. | The page title should change to 'Quant Catalog Login'. | is_login_link_works
The homepage link must navigate back to the index page correctly. | When the homepage link on the index page is clicked. | The page title should change to 'Quant Catalog Home'. | is_homepage_link_works
The strategies link must navigate to the strategies page correctly. | When the strategies link on the index page is clicked. | The page title should change to 'Quant Catalog Strategies'. | is_strategies_link_works
The markets link must navigate to the market detail page correctly. | When the markets link on the index page is clicked. | The page title should change to 'Quant Catalog  Stocks'. | is_market_link_works
The CAGR link must navigate to the CAGR page correctly. | When the CAGR link on the index page is clicked. | The page title should change to 'Quant Catalog CAGR'. | is_cagr_link_works
The Sharpe link must navigate to the Sharpe page correctly. | When the Sharpe link on the index page is clicked. | The page title should change to 'Quant Catalog Sharpe'. | is_sharpe_link_works
The Long Only link must navigate to the Long Only page correctly. | When the Long Only link on the index page is clicked. | The page title should change to 'Quant Catalog Long Only'. | is_long_link_works

#### Signup Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The signup page must display the correct title. | When the signup page is loaded. | The page title should be 'Quant Catalog Signup'. | is_title_matches
The signup form must process input data correctly. | When valid data is entered into the signup form and submitted. | The page title should change to 'Quant Catalog | Login'. | is_signup_form_works

#### Login Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The login page must display the correct title. | When the login page is loaded. | The page title should be 'Quant Catalog Login'. | is_title_matches
The login form must process input data correctly. | When valid credentials are entered into the login form and submitted. | The text 'LOGOUT' should be visible on the page. | is_login_form_works
The logout link must navigate back to the index page correctly. | When the logout link is clicked. | The page title should change to 'Quant Catalog Home'. | is_logout_link_works

#### Create Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The create page must display the correct title. | When the create page is loaded. | The page title should be 'Quant Catalog Create Strategy'. | is_title_matches
The create form must process input data correctly. | When valid strategy details are entered into the create form and submitted. | The message 'Strategy was created successfully' should be visible. | is_create_form_works

#### Update Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The update page must display the correct title. | When the update page is loaded. | The page title should be 'Quant Catalog Update Strategy'. | is_title_matches
The update form must process input data correctly. | When updates are made to a strategy and the form is submitted. | The message 'Strategy was updated successfully' should be visible. | is_update_form_works

#### Delete Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The delete form must process the deletion of a strategy correctly. | When valid credentials are entered, and a strategy is selected for deletion. | The message 'Strategy was deleted successfully' should be visible. | is_delete_form_works

#### Strategies Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The strategies page must display the correct title. | When the strategies page is loaded. | The page title should be 'Quant Catalog Strategies'. | is_title_matches
The strategies page must display the correct heading. | When the strategies page is loaded. | The heading should be 'MOMENTUM'. | is_strategies_heading_displayed_correctly

#### Strategies Detail Page Requirements

Requirement | Condition | Expected Outcome | Test Case
----------- | --------- | ---------------- | ---------
The strategies detail page must display the correct title. | When the strategies detail page is loaded. | The page title should be 'Quant Catalog Momentum'. | is_title_matches
The strategies detail page must display the correct heading. | When the strategies detail page is loaded. | The heading should be 'DETAILED INFORMATION ABOUT MOMENTUM'. | is_strategies_detail_heading_displayed_correctly
