CODING IN LOGIN SCREEN:-
Public Class Form1
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        If TextBox1.Text = "admin" And TextBox2.Text = "password" Then
            MsgBox("UserName and Password Accepted")
            mainmenu.Show()

        Else
            MsgBox("You have entered wrong Username or Password")
        End If

    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
        TextBox1.Clear()
        TextBox2.Clear()
    End Sub
    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        MsgBox("Thanks for using Airline Reservation System ")

        Me.Close()
    End Sub
End Class

CODING IN MAIN MENU
Public Class mainmenu
    Private Sub ExitToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ExitToolStripMenuItem.Click
        Me.Close()
    End Sub

    Private Sub FareDetailToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles FareDetailToolStripMenuItem.Click
        faredetails.Show()
    End Sub

    Private Sub TicketReservationToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TicketReservationToolStripMenuItem.Click
        Ticketreservation.Show()
    End Sub

    Private Sub AddNewToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddNewToolStripMenuItem.Click
        customerdetails.Show()
    End Sub

    Private Sub DeleteToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles DeleteToolStripMenuItem.Click
        Delcustomer.Show()
    End Sub

    Private Sub UpdateToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles UpdateToolStripMenuItem.Click
        updatecustomer.Show()
    End Sub

    Private Sub AddNewToolStripMenuItem1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles AddNewToolStripMenuItem1.Click
        flightdetails.Show()
    End Sub

    Private Sub DeleteToolStripMenuItem1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles DeleteToolStripMenuItem1.Click
        Delflight.Show()
    End Sub

    Private Sub UpdateToolStripMenuItem1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles UpdateToolStripMenuItem1.Click
        Updateplane.Show()
    End Sub

    Private Sub TicketCancellationToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TicketCancellationToolStripMenuItem.Click
        TicketCancellation.Show()

    End Sub

    Private Sub ReservationEnquiryToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles ReservationEnquiryToolStripMenuItem.Click
        TicketEnquiry.Show()
    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
        Me.Close()
    End Sub

    Private Sub CustomersToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
        customerdetails.Show()

    End Sub

    Private Sub FlightsToolStripMenuItem_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
        flightdetails.Show()

    End Sub
End Class

CODING IN ADD NEW CUSTOMER:-
Imports System.Data
Imports System
Imports System.Collections
Imports System.Console
Imports System.Linq
Imports System.Web
Imports System.Data.SqlClient


Public Class customerdetails

    Private Sub Button5_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button5.Click
        If TextBox1.Text = "" Or TextBox2.Text = "" Or TextBox7.Text = "" Or TextBox4.Text = "" Then
            MsgBox("fill the information properly")
        ElseIf IsNumeric(TextBox1.Text) Then
            MsgBox("name should not be numeric")
        ElseIf IsInputChar(TextBox4.Text) Then
            MsgBox("contct should not be char")
        ElseIf IsNumeric(TextBox2.Text) Then
            MsgBox(" Father's name should not be numeric")
        ElseIf IsInputChar(TextBox6.Text) Then
            MsgBox("Insert D_O_B")
        ElseIf IsNumeric(TextBox7.Text) Then
            MsgBox("address should not be numeric")
            Me.Hide()

        End If


        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")
        con.Open()

        Dim PassportNo As String
        PassportNo = Format(DateTime.Now, "yyyyMMddhhmmss")
        Label4.Text = PassportNo

        Dim cmd As New SqlCommand("insert into customer_dtls values(@passportno,@custname,@fathername,@d_o_b,@address,@contactno)", con)
        cmd.CommandType = CommandType.Text

        cmd.Parameters.Add("@passportNo", SqlDbType.VarChar, 50).Value = PassportNo
        cmd.Parameters.Add("@custname", SqlDbType.VarChar, 50).Value = TextBox1.Text
        cmd.Parameters.Add("@fathername", SqlDbType.VarChar, 50).Value = TextBox2.Text
        cmd.Parameters.Add("@d_o_b", SqlDbType.DateTime).Value = TextBox6.Text
        cmd.Parameters.Add("@address", SqlDbType.VarChar, 50).Value = TextBox7.Text
        cmd.Parameters.Add("@contactno", SqlDbType.VarChar, 50).Value = TextBox4.Text
        cmd.ExecuteNonQuery()
        cmd.Dispose()
        con.Close()
        MsgBox("welcome you are now the customer of airline")

    End Sub

    Private Sub Button1_Click_1(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click

        mainmenu.Show()
        Me.Hide()


    End Sub

    
    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        TextBox1.Clear()
        TextBox2.Clear()
        TextBox4.Clear()
        TextBox6.Clear()
        TextBox7.Clear()
    End Sub

    Private Sub TextBox6_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox6.TextChanged
        If TextBox6.Text = "" Then
            MsgBox("Insert D_O_B")

        End If

    End Sub

    Private Sub TextBox7_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox7.TextChanged
        If TextBox7.Text = "" Then
            MsgBox("Insert Address")
        End If
    End Sub

    Private Sub TextBox4_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox4.TextChanged
        If TextBox4.Text = "" Then
            MsgBox("Insert Contact_No")
        End If
    End Sub

    Private Sub TextBox2_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox2.TextChanged
        If TextBox2.Text = "" Then
            MsgBox("Insert Father's Name")
        End If
    End Sub

    Private Sub TextBox1_TextChanged(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles TextBox1.TextChanged
        If TextBox1.Text = "" Then
            MsgBox("Insert Your Name")
        End If
    End Sub
End Class

CODING IN UPDATE CUSTOMER:-
Imports System.Data
Imports System
Imports System.Collections
Imports System.Console
Imports System.Linq
Imports System.Web
Imports System.Data.SqlClient
Public Class updatecustomer

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
        Me.Close()
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")

        con.Open()
        Dim adp As SqlDataReader

        Dim cmd As New SqlCommand("select * from customer_dtls where passportNo=" + "'" + ComboBox1.Text + "'", con)
        adp = cmd.ExecuteReader()
        While adp.Read
            TextBox2.Text = adp(1)
            TextBox3.Text = adp(2)
            TextBox4.Text = adp(3)
            TextBox5.Text = adp(4)
            TextBox6.Text = adp(5)
        End While
        adp.Close()
        con.Close()
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")
        con.Open()
        Dim cmd As New SqlCommand("Update customer_dtls set CustName=" + "'" + TextBox2.Text + "'" + "," + "Fathername=" + "'" + TextBox3.Text + "'" + "," + "D_O_B=" + "'" + TextBox4.Text + "'" + "," + "Address=" + "'" + TextBox5.Text + "'" + "," + "ContactNo=" + "'" + TextBox6.Text + "'" + "where PassportNo=" + "'" + ComboBox1.Text + "'", con)
        cmd.CommandType = CommandType.Text

        cmd.ExecuteNonQuery()
        cmd.Dispose()
        con.Close()
        MsgBox("updated")
    End Sub

    Private Sub updatecustomer_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")

        con.Open()
        Dim adp As SqlDataReader

        Dim cmd As New SqlCommand("select * from customer_dtls", con)
        adp = cmd.ExecuteReader()
        While adp.Read
            ComboBox1.Items.Add(adp(0))
        End While
        adp.Close()
    End Sub

    Private Sub Button1_Click_1(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        mainmenu.Show()
        Me.Close()
    End Sub
End Class

CODING IN FLIGHT DETAILS:-

Imports System.Data
Imports System
Imports System.Collections
Imports System.Console
Imports System.Linq
Imports System.Web
Imports System.Data.SqlClient

Public Class flightdetails

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")
        con.Open()

        Dim cmd As New SqlCommand("insert into Flight_dtls values(@flightname,@flightcode,@classname,@totalseats,@flightsource,@flightdestination,@departure,@arrival,@fare)", con)
        cmd.CommandType = CommandType.Text

        cmd.Parameters.Add("@flightname", SqlDbType.VarChar, 50).Value = TextBox1.Text
        cmd.Parameters.Add("@flightcode", SqlDbType.VarChar, 50).Value = TextBox2.Text
        cmd.Parameters.Add("@classname", SqlDbType.VarChar, 50).Value = TextBox3.Text
        cmd.Parameters.Add("@totalseats", SqlDbType.VarChar, 50).Value = TextBox4.Text
        cmd.Parameters.Add("@flightsource", SqlDbType.VarChar, 50).Value = TextBox5.Text
        cmd.Parameters.Add("@flightdestination", SqlDbType.VarChar, 50).Value = TextBox6.Text
        cmd.Parameters.Add("@departure", SqlDbType.VarChar, 50).Value = TextBox7.Text
        cmd.Parameters.Add("@arrival", SqlDbType.VarChar, 50).Value = TextBox8.Text
        cmd.Parameters.Add("@fare", SqlDbType.VarChar, 50).Value = TextBox9.Text

        cmd.ExecuteNonQuery()
        cmd.Dispose()
        con.Close()
        MsgBox("welcome in airline....new flight has been Added")




    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        TextBox1.Clear()
        TextBox2.Clear()
        TextBox3.Clear()
        TextBox4.Clear()
        TextBox5.Clear()
        TextBox6.Clear()
    End Sub

    Private Sub Button1_Click_1(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        mainmenu.Show()
        Me.Hide()
    End Sub
End Class
CODING IN UPDATE Plane
Imports System.Data
Imports System
Imports System.Collections
Imports System.Console
Imports System.Linq
Imports System.Web
Imports System.Data.SqlClient
Public Class Updateplane
    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
        Me.Close()
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")
        con.Open()
        Dim cmd As New SqlCommand("Update flight_dtls set flightcode=" + "'" + TextBox2.Text + "'" + "," + "classname=" + "'" + TextBox3.Text + "'" + "," + "totalseats=" + "'" + TextBox4.Text + "'" + "," + "flightsource=" + "'" + TextBox5.Text + "'" + "," + "flightdestination=" + "'" + TextBox6.Text + "'" + "where flightname=" + "'" + ComboBox1.Text + "'", con)
        cmd.CommandType = CommandType.Text

        cmd.ExecuteNonQuery()
        cmd.Dispose()
        con.Close()
        MsgBox("updated")



    End Sub

    Private Sub Updateplane_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")

        con.Open()
        Dim adp As SqlDataReader

        Dim cmd As New SqlCommand("select * from flight_dtls", con)
        adp = cmd.ExecuteReader()
        While adp.Read
            ComboBox1.Items.Add(adp(0))
        End While
        adp.Close()
        con.Close()
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")

        con.Open()
        Dim adp As SqlDataReader

        Dim cmd As New SqlCommand("select * from flight_dtls where flightname=" + "'" + ComboBox1.Text + "'", con)
        adp = cmd.ExecuteReader()
        While adp.Read
            TextBox2.Text = adp(1)
            TextBox3.Text = adp(2)
            TextBox4.Text = adp(3)
            TextBox5.Text = adp(4)
            TextBox6.Text = adp(5)
            TextBox1.Text = adp(6)
            TextBox7.Text = adp(7)
            TextBox8.Text = adp(8)
        End While
        adp.Close()
        con.Close()

    End Sub

    Private Sub Button1_Click_1(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        mainmenu.Show()
        Me.Close()
    End Sub
End Class


CODING IN TICKET RESERVATION
Imports System.Data
Imports System
Imports System.Collections
Imports System.Console
Imports System.Linq
Imports System.Web
Imports System.Data.SqlClient
Public Class Ticketreservation


    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        If ComboBox5.SelectedItem = 5 Then
            TextBox17.Text = 5 * TextBox5.Text
        ElseIf ComboBox5.SelectedItem = 4 Then
            TextBox17.Text = 4 * TextBox5.Text
        ElseIf ComboBox5.SelectedItem = 3 Then
            TextBox17.Text = 3 * TextBox5.Text
        ElseIf ComboBox5.SelectedItem = 2 Then
            TextBox17.Text = 2 * TextBox5.Text
        ElseIf ComboBox5.SelectedItem = 1 Then
            TextBox17.Text = 1 * TextBox5.Text
        End If
    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
        Me.Close()
    End Sub

    Private Sub Ticketreservation_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")
        con.Open()
        Dim adp As SqlDataReader
        Dim cmd As New SqlCommand("select * from flight_dtls", con)
        adp = cmd.ExecuteReader()
        While adp.Read
            ComboBox1.Items.Add(adp(0))
        End While
        adp.Close()
        con.Close()
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        '' Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")
        'con.Open()
        'Dim cmd As New SqlCommand("insert into ticket_dtls values(@ticketNumber,@customername,@Ticketreaservation)", con)
        'cmd.CommandType = CommandType.Text
        '
        '       Dim TicketNumber As String
        '       TicketNumber = Format(DateTime.Now, "yyyyMMddhhmmss")
        '      Label4.Text = TicketNumber
        '     cmd.ExecuteNonQuery()
        '    cmd.Dispose()
        '   con.Close()
        MsgBox("Ticket reserved")
    End Sub

    Private Sub Button2_Click_1(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        mainmenu.Show()
        Me.Close()

    End Sub

    Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button4.Click
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")
        con.Open()
        Dim adp As SqlDataReader
        Dim cmd As New SqlCommand("select * from flight_dtls where flightname=" + "'" + ComboBox1.Text + "'", con)
        adp = cmd.ExecuteReader()
        While adp.Read
            TextBox1.Text = adp(6)
            TextBox2.Text = adp(7)
            TextBox3.Text = adp(4)
            TextBox4.Text = adp(5)
            TextBox5.Text = adp(8)
            TextBox22.Text = adp(2)
        End While
        adp.Close()
        con.Close()
    End Sub
End Class
CODING IN TICKET CANCELLATION
Imports System.Data
Imports System
Imports System.Collections
Imports System.Console
Imports System.Linq
Imports System.Web
Imports System.Data.SqlClient
Public Class TicketCancellation

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        TextBox5.Text = TextBox4.Text * 20 / 100
        TextBox6.Text = TextBox4.Text - TextBox5.Text

    End Sub

    Private Sub Button4_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
        Me.Close()

    End Sub

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")

        con.Open()
        Dim adp As SqlDataReader
        Dim cmd As New SqlCommand("select * from Cancel where TicketNumber=" + "'" + ComboBox1.Text + "'", con)
        adp = cmd.ExecuteReader()
        While adp.Read
            TextBox2.Text = adp(1)
            TextBox3.Text = adp(2)
            TextBox4.Text = adp(3)
        End While
        adp.Close()
        con.Close()

    End Sub

    Private Sub TicketCancellation_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")

        con.Open()
        Dim adp As SqlDataReader

        Dim cmd As New SqlCommand("select * from Cancel", con)
        adp = cmd.ExecuteReader()
        While adp.Read
            ComboBox1.Items.Add(adp(0))
        End While
        adp.Close()
    End Sub

    Private Sub Button3_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button3.Click
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")
        con.Open()
        Dim cmd As New SqlCommand("delete from cancel where TicketNumber=" & "'" & ComboBox1.Text & "'", con)
        cmd.CommandType = CommandType.Text

        cmd.ExecuteNonQuery()
        cmd.Dispose()
        con.Close()
        MsgBox("Ticket Cancelled")
    End Sub
End Class
CODING IN TICKET ENQUIRY
Imports System.Data
Imports System
Imports System.Collections
Imports System.Console
Imports System.Linq
Imports System.Web
Imports System.Data.SqlClient
Public Class TicketEnquiry

    Private Sub Button2_Click(ByVal sender As System.Object, ByVal e As System.EventArgs)
        Me.Close()
    End Sub

    Private Sub Button2_Click_1(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button2.Click
        mainmenu.Show()
        Me.Close()

    End Sub

    Private Sub Button1_Click(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles Button1.Click
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")

        con.Open()
        Dim adp As SqlDataReader

        Dim cmd As New SqlCommand("select * from cancel where TicketNumber=" + "'" + ComboBox1.Text + "'", con)
        'Dim cmd As New SqlCommand("select * from flight_dtls where TicketNumber=" + "'" + ComboBox1.Text + "'", con)
        adp = cmd.ExecuteReader()

        While adp.Read
            TextBox2.Text = adp(1)
            TextBox3.Text = adp(2)
            TextBox4.Text = adp(3)
            TextBox5.Text = adp(4)
            TextBox6.Text = adp(5)
        End While
        adp.Close()
        con.Close()
    End Sub

    Private Sub TicketEnquiry_Load(ByVal sender As System.Object, ByVal e As System.EventArgs) Handles MyBase.Load
        Dim con As New SqlConnection("server=SAHIL-PC;database=D:\Airline Reservation System - Copy\Airline Reservation System\data\dbARS.mdf;Integrated Security=True")

        con.Open()
        Dim adp As SqlDataReader

        'Dim cmd As New SqlCommand("select * from cancel", con)
        Dim cmd As New SqlCommand("select * from flight_dtls", con)
        adp = cmd.ExecuteReader()
        While adp.Read
            ComboBox1.Items.Add(adp(0))
        End While
        adp.Close()
        con.Close()
    End Sub
End Class
