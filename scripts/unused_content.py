from datetime import datetime, timedelta
import pytz
#set utc timezone awarness
utc=pytz.UTC

### UPDATE THIS PARAM ### find looks that haven't been accessed in X days
day = 100

unused_content = {}
last_accessed = []
content_id = []
title = []
def unused_looks(day):
    for i in sdk.all_looks(fields='id, title, last_accessed_at'):
        #check to make sure the look has been accessed at least once
        if i.last_accessed_at is not None:
            #log instances where days since access is greater than the set days we're looking for
            if (utc.localize(datetime.now()) - i.last_accessed_at.replace(tzinfo=utc)).days > day:
                last_accessed.append(i.last_accessed_at)
                content_id.append(i.id)
                title.append(i.title)
            else:
                pass
        else:
            pass
    
    unused_content['content_id'] = look_id
    unused_content['title'] = look_id
    unused_content['last_accessed'] = look_id
    return unused_content
    
def unused_dashboards(day):
    for i in sdk.search_dashboards(fields='id, title, last_accessed_at'):
        #check to make sure the look has been accessed at least once
        if i.last_accessed_at is not None:
            #log instances where days since access is greater than the set days we're looking for
            if (utc.localize(datetime.now()) - i.last_accessed_at.replace(tzinfo=utc)).days > day:
                last_accessed.append(i.last_accessed_at)
                content_id.append(i.id)
                title.append(i.title)
            else:
                pass
        else:
            pass
    unused_content['content_id'] = look_id
    unused_content['title'] = look_id
    unused_content['last_accessed'] = look_id
    return unused_content
    
    
unused_looks(day)
unused_dashboards(day)