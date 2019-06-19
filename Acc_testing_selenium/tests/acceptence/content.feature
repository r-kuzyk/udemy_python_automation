Feature: Test that page have correct content
  Scenario: Blog page has a correct title
    Given I am on the blog page
    Then There is a title shown on the page
    And The title tag has content "This is a blog page"


  Scenario: Blog page has a correct title
    Given I am on the home page
    Then There is a title shown on the page
    And The title tag has content "This is a blog page"


  Scenario: Blog page loads the post
    Given I am on the blog page
    And I wait for the post to load
    Then I can see there is a posts section on the page

  Scenario: User Can create a new post
    Given I am on the new post page
    When I enter "Some text" in the title field
    And I enter "Test Content" in the content field
    And I press the submit button
    Then I am on the blog page
    Given I wait for the post to load
    Then I can see there is a post with the title "Test Post" in the post section