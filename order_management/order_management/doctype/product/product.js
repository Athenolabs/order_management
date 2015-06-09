frappe.ui.form.on("Product", "onload", function(frm) {
	function put_attachments() {
		if(!frm.attachments.get_attachments()) {
			return
		}
		attachments = $.map(frm.attachments.get_attachments(), function(i, x) {
			return x.file_url
		});
		console.log(attachments);
	}
	setTimeout(300, put_attachments)
})
