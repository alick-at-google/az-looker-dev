import looker_sdk
###################log into 7.6 instance################################
sdk_old = looker_sdk.init31(config_file="looker.ini", section="firehouse_old")

#input dashboard_ids we want queries of 
old_dash_id = "28"

#object filled with queries from 7.6
qq = []
#go through all tiles on dashboard
for i in test.dashboard(dash).dashboard_elements:
    #if tile has a query (ie.is a visualization)
    if(i.query != None):
        #and query is a table vis
        if i.query.vis_config["type"] == "looker_grid":
            qq.append(models.WriteQuery(
                        model=i.query.model,
                        view=i.query.view,
                        fields=i.query.fields,
                        pivots=i.query.pivots,
                        filters=i.query.filters,
                        sorts=i.query.sorts,
                        limit=i.query.limit,
                        column_limit=i.query.column_limit,
                        total=i.query.total,
                        row_total=i.query.row_total,
                        subtotals=i.query.subtotals,
                        vis_config=i.query.vis_config))
            
            
######################## log into prod instance##########################
sdk_new = looker_sdk.init31(config_file="looker.ini", section="firehouse_prod")

q_object = []
# take query object from 7.6 instance and make them in the 7.14 instance
for i in qq:
    q_object.append(sdk_new.create_query(i))
    
    
#dashboard id in prod instance    
new_dash_id = "28"

#make dashboard element
dashboard_element = looker_sdk.models.WriteDashboardElement(
  dashboard_id= new_dash_id,
  query_id= q_object[1].id
  )
#update dashboard tile in prod with the exact configurations from 7.6 query
sdk_new.update_dashboard_element(sdk_new.dashboard(new_dash_id).dashboard_elements[2].id, dashboard_element)