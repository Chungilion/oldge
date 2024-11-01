# ---------------------------------------------------------------------------
# build_b5_ne_50m_admin_0_tiny_countries.py
# Created on: Sat Aug 19 2017 11:47:23 PM
#   (generated by ArcGIS/ModelBuilder)
# ---------------------------------------------------------------------------

# Import system modules
import sys, string, os, arcgisscripting

# Create the Geoprocessor object
gp = arcgisscripting.create()

# Set the necessary product code
gp.SetProduct("ArcInfo")

# Load required toolboxes...
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Data Management Tools.tbx")
gp.AddToolbox("C:/Program Files/ArcGIS/ArcToolbox/Toolboxes/Analysis Tools.tbx")


# Local variables...
ne_50m_admin_0_tiny_countries_shp__2_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_tiny_countries.shp"
ne_admin_0_details_level_4_subunits_dbf = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\housekeeping\\ne_admin_0_details_level_4_subunits.dbf"
ne_50m_admin_0_tiny_countries_scale_rank_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_tiny_countries_scale_rank.shp"
ne_50m_admin_0_tiny_countries_shp__4_ = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_tiny_countries.shp"
ne_50m_admin_0_tiny_countries_shp = "C:\\ProjectFiles\\NaturalEarth\\nev_version_4d0d0\\50m_cultural\\ne_50m_admin_0_tiny_countries.shp"

# Process: Select...
gp.Select_analysis(ne_50m_admin_0_tiny_countries_scale_rank_shp, ne_50m_admin_0_tiny_countries_shp, "\"scalerank\" >= 0")

# Process: Join Field...
gp.JoinField_management(ne_50m_admin_0_tiny_countries_shp, "sr_su_a3", ne_admin_0_details_level_4_subunits_dbf, "su_a3", "")

# Process: Delete Field (2)...
gp.DeleteField_management(ne_50m_admin_0_tiny_countries_shp__2_, "sr_sov_a3;sr_adm0_a3;sr_gu_a3;sr_su_a3;sr_subunit;labelrank;MIN_scaler")

