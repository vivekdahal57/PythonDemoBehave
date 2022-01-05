#Feature: Smoke Test execution
#
#  Scenario: User succeed to login in Blueprint
#    Given user is in blueprint Login page
#    When user use correct_username and correct_password
#    Then user succeed to login
#    Then user succeed to logout
#
#  Scenario: User succeed to login in Django Admin
#    Given user is in admin Login page
#    When admin user use admin_username and admin_password
#    Then admin user succeed to login
#    Then admin user succeed to logout
#
#  Scenario: Normal User cannot access admin panel
#    Given user is in blueprint Login page
#    When user use correct_username and correct_password
#    Then user succeed to login
#    Then user is in admin Login page
#    Then normal user correct_username failed to authorized
#
#  Scenario: Admin User able to create inactive user
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user creates a inactive user with username created_username and password created_password
#    Then admin user succeed to logout
#    Then inactive user with username created_username and password created_password is not able to login
#
#  Scenario: Admin User able to edit inactive user to active
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user changes a inactive user to active with username created_username
#    Then admin user succeed to logout
#    Then user with username created_username and password created_password is able to login
#    Then user succeed to logout
#
#  Scenario: Created user can be deleted by admin user
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can delete created_username user
#    Then admin user succeed to logout
#    Then deleted user with username created_username and password created_password cannot login
#
#  Scenario: User creates a collection with suffix 1
#    Given user is in blueprint Login page
#    When user use correct_username and correct_password
#    Then user succeed to login
#    Then logged in user can create collection with name automation_collection1 and with file goodtxt.txt
#    Then user succeed to logout
#
#  Scenario: User creates a collection with suffix 2
#    Given user is in blueprint Login page
#    When user use correct_username and correct_password
#    Then user succeed to login
#    Then logged in user can create collection with name automation_collection2 and with file zipfile.zip
#    Then user succeed to logout
#
#  Scenario: Admin User is able to create cluster with suffix 1
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user creates a cluster with name automation_cluster1 cluster for automation_collection1 collection and Pending status
#    Then admin user can change a cluster with name automation_cluster1 cluster for automation_collection1 collection and Proposed status
#    Then admin user succeed to logout
#
#  Scenario: Admin User is able to create cluster with suffix 2
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user creates a cluster with name automation_cluster2 cluster for automation_collection2 collection and Pending status
#    Then admin user can change a cluster with name automation_cluster2 cluster for automation_collection2 collection and Proposed status
#    Then admin user succeed to logout
#
#  Scenario: User search for files in the collection
#    Given user is in blueprint Login page
#    When user use correct_username and correct_password
#    Then user succeed to login
#    Then logged in user can search with filename goodtxt.txt and land on it
#    Then user succeed to logout
#
#  Scenario: User search for automation_collection1 in dashboard and lands on details page
#    Given user is in blueprint Login page
#    When user use correct_username and correct_password
#    Then user succeed to login
#    Then logged in user can search with collection name automation_collection1 and lands on collection details page
#    Then user succeed to logout
#
#  Scenario: Staff User can assign batch to the cluster1
#    Given user is in blueprint Login page
#    When user use admin_username and admin_password
#    Then user succeed to login
#    Then user navigate to Architect application
#    Then user can drag transfer-batch to automation_cluster1 after selecting automation_collection1
#    Then user can create a draft plan for collection automation_collection1 and for cluster automation_cluster1
#    Then user can create a new step with Bounding Box for goodtxt.txt file for collection automation_collection1 and cluster automation_cluster1
#    Then user succeed to logout from architect application
#
#  Scenario: Admin user can verify draft ingest plan from admin panel for cluster1
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can navigate to ingest plans and verify draft plan for automation_cluster1
#    Then admin user succeed to logout
#
#  Scenario: Admin user can verify completed ingested result from admin panel for cluster1
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can navigate to ingest plans and get plan name for automation_cluster1
#    Then admin user can navigate to ingest result and verify completed ingest result
#    Then admin user succeed to logout
#
#  Scenario: Admin User is able to update cluster1
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can change a cluster with name automation_cluster1 cluster for automation_collection1 collection and Active status
#    Then admin user succeed to logout
#
#  Scenario: User search for collection1 in dashboard and download file
#    Given user is in blueprint Login page
#    When user use correct_username and correct_password
#    Then user succeed to login
#    Then logged in user can search with collection name automation_collection1 and lands on collection details page
#    Then user can download structured files from the collection details page using correct_password
#    Then user succeed to logout
#
#  Scenario: User search for files in the collection2
#    Given user is in blueprint Login page
#    When user use correct_username and correct_password
#    Then user succeed to login
#    Then logged in user can search with filename img.PNG and land on it
#    Then user succeed to logout
#
#  Scenario: User search for automation_collection2 in dashboard and lands on details page
#    Given user is in blueprint Login page
#    When user use correct_username and correct_password
#    Then user succeed to login
#    Then logged in user can search with collection name automation_collection2 and lands on collection details page
#    Then user succeed to logout
#
#  Scenario: Staff User can assign batch to the cluster2
#    Given user is in blueprint Login page
#    When user use admin_username and admin_password
#    Then user succeed to login
#    Then user navigate to Architect application
#    Then user can drag transfer-batch to automation_cluster2 after selecting automation_collection2
#    Then user can create a draft plan for collection automation_collection2 and for cluster automation_cluster2
#    Then user can create a new step with Bounding Box for img.PNG file for collection automation_collection2 and cluster automation_cluster2
#    Then user succeed to logout from architect application
#
#  Scenario: Admin user can verify draft ingest plan from admin panel for cluster2
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can navigate to ingest plans and verify draft plan for automation_cluster2
#    Then admin user succeed to logout
#
#  Scenario: Admin user can verify completed ingested result from admin panel for cluster2
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can navigate to ingest plans and get plan name for automation_cluster2
#    Then admin user can navigate to ingest result and verify completed ingest result
#    Then admin user succeed to logout
#
#  Scenario: Admin User is able to update cluster2
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can change a cluster with name automation_cluster2 cluster for automation_collection2 collection and Active status
#    Then admin user succeed to logout
#
#  Scenario: User search for collection2 in dashboard and download file
#    Given user is in blueprint Login page
#    When user use correct_username and correct_password
#    Then user succeed to login
#    Then logged in user can search with collection name automation_collection2 and lands on collection details page
#    Then user can download structured files from the collection details page using correct_password
#    Then user succeed to logout
#
#  Scenario: Admin user can delete draft ingest plan from admin panel
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can delete ingest draft plan created for cluster automation_cluster1
#    Then admin user succeed to logout
#
#  Scenario: Created cluster1 can be deleted by admin user
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can delete a cluster with name automation_cluster1
#    Then admin user succeed to logout
#
#  Scenario: Created cluster2 can be deleted by admin user
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can delete a cluster with name automation_cluster2
#    Then admin user succeed to logout
#
#  Scenario: Created collection1 can be deleted by admin user
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can delete automation_collection1 collection
#    Then admin user succeed to logout
#
#  Scenario: Created collection2 can be deleted by admin user
#    Given admin user is in dashboard page after login with admin_username and admin_password
#    When admin user can delete automation_collection2 collection
#    Then admin user succeed to logout