import win32com.client

xl = win32com.client.Dispatch("Excel.Application")
xl.
xlns =  win32com.client.Dispatch("Microsoft.Office.Tools.Excel")
win32com.client.
wb = xl.Workbooks.Add()
wb.Queries.Add('two',' let Source = Exchange.Contents("akickha2@scj.com"){[Name="Mail"]}[Data] in Mail1')

wb.Connections.Add2({    "Name": "M",    "Description" : "",    "ConnectionString" : "OLEDB;Provider=Microsoft.Mashup.OleDb.1;Data Source=$Workbook$;Location=Mail",    "CommandText": "Select * from [two]"        })Microsoft.Office.Interop.Excel


