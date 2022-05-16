///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Jun 17 2015)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __NONAME_H__
#define __NONAME_H__

#include <wx/artprov.h>
#include <wx/xrc/xmlres.h>
#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/textctrl.h>
#include <wx/sizer.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class modbusApp
///////////////////////////////////////////////////////////////////////////////
class modbusApp : public wxFrame 
{
	private:
	
	protected:
		wxStaticText* m_staticText_PRM;
		wxTextCtrl* m_textCtrl_PRM;
	
	public:
		
		modbusApp( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("modbus app"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 901,351 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		
		~modbusApp();
	
};

#endif //__NONAME_H__
