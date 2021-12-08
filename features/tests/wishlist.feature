# Created by jessi at 12/7/2021
Feature: Test cases for wishlist functionality

  Scenario: Empty wishlist shows "No products added to the wishlist" text
    Given Open Gettop wishlist page
    Then Verify No products added to the wishlist text is displayed
