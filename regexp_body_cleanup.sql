 update tbody2 set body = regexp_replace(body,
 <-- regexp -->
,'')


-- REGEXP FOR DELETION
'From.*(\n|\r\n|\v)*Sent:.*M(\n|\r\n|\v)*To:.*(\n|\r\n|\v)*(?=Subject)'
'^\\t?From:.*(\\n|\\r\\n)?Sent:.*M(\\n|\\r\\n)?To:.*(\\n|\\r\\n)*((Cc.*)(\\n|\\r\\n)?){0,1}Subject:.*(\\n|\\r\\n)'
'\t?CONFIDENTIALITY NOTICE:.*(\n|\r\n)';