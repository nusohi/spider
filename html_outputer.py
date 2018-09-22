#coding:utf-8
class HtmlOutputer(object):

    def __init__(self):
        self.datas = []

    def collect_data(self, data):
        if data is None:
            return
        self.datas.append(data)

    def output_html(self):
        fout = open('output.html', mode='w')

        fout.write("<meta charset=\"utf-8\">")
        fout.write("<html>")
        fout.write("<body>")
        fout.write("<table border=\"1\">")
        fout.write("<th>title</th><th>summary</th>")

        for data in self.datas:
            fout.write("<tr>")
            fout.write("<td><a href=\"%s\" target=\"_blank\">%s</a></td>" %(data['url'].encode('utf-8'), data['title'].encode('utf-8')))
            fout.write("<td>%s</td>" %(data['summary'].encode('utf-8')))
            fout.write("</tr>")

        fout.write("</table>")
        fout.write("</body>")
        fout.write("</html>")

        fout.close()
