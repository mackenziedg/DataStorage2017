# DSR_Project1
Repository for the first project in the Data Storage and Retrieval class. Fall 2017.

Deadline is October 31st (or 3 weeks, roughly).
 
## Installation
 
 * Create a virtual Python environment with `virtualenv`. Run `python package_and_run.py` to package the app and start the server. This also sets the environment variables needed for `flask` to run, so as of right now this script needs to run every time to start up the server.
 
* Shared the `config.py` file on Google Drive, which goes in `<project root>/h1b/instance/`. There is another `config.py` in `/h1b/`.


## Data Source

Data was pulled from 

* http://www.flcdatacenter.com/caseh1b.aspx
  * under heading "H-1B EFile Data" years 2002-2006

and 

* https://www.foreignlaborcert.doleta.gov/performancedata.cfm
  * under "Disclosure Data" -> "LCA Programs (H-1B, H-1B1, E-3)" -> years 2008-2016
  * and "Disclosure Data" -> "Latest Quarterly Updates" -> H-1B for FY1 (this location could potentially change in the future if a new fiscal year is the latest)
