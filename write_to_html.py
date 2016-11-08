def main():
    out = open("compare.html","w+")
    data = open("compare.csv")
    num_lines = len(data.readlines()) - 1
    data.close()
    data = open("compare.csv")
    
    out.write("<!DOCTYPE html>\n")
    out.write("<meta charset=\"utf-8\">\n")
    out.write("<style>\n")
    out.write("\n")
    out.write("body {\n")
    out.write("  font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n")
    out.write("  width: 2560px;\n")
    out.write("  height: 1080px;\n")
    out.write("  position: relative;\n")
    out.write("}\n")
    out.write("\n")
    out.write("svg {\n")
    out.write("    width: 100%;\n")
    out.write("    height: 100%;\n")
    out.write("    position: center;\n")
    out.write("}\n")
    out.write("\n")
    out.write("text{\n")
    out.write("    font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n")
    out.write("}\n")
    out.write("\n")
    out.write(".toolTip {\n")
    out.write("    font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n")
    out.write("    position: absolute;\n")
    out.write("    display: none;\n")
    out.write("    width: auto;\n")
    out.write("    height: auto;\n")
    out.write("    background: none repeat scroll 0 0 white;\n")
    out.write("    border: 0 none;\n")
    out.write("    border-radius: 8px 8px 8px 8px;\n")
    out.write("    box-shadow: -3px 3px 15px #888888;\n")
    out.write("    color: black;\n")
    out.write("    font: 12px sans-serif;\n")
    out.write("    padding: 5px;\n")
    out.write("    text-align: center;\n")
    out.write("}\n")
    out.write("\n")
    out.write(".legend {\n")
    out.write("    font-family: \"Helvetica Neue\", Helvetica, Arial, sans-serif;\n")
    out.write("    font-size: 60%;\n")
    out.write("}\n")
    out.write("\n")
    out.write("rect {\n")
    out.write("    stroke-width: 2;\n")
    out.write("}\n")
    out.write("\n")
    out.write("text {\n")
    out.write("  font: 10px sans-serif;\n")
    out.write("}\n")
    out.write("\n")
    out.write(".axis text {\n")
    out.write("  font: 10px sans-serif;\n")
    out.write("}\n")
    out.write("\n")
    out.write(".axis path{\n")
    out.write("  fill: none;\n")
    out.write("  stroke: #000;\n")
    out.write("}\n")
    out.write("\n")
    out.write(".axis line {\n")
    out.write("  fill: none;\n")
    out.write("  stroke: #000;\n")
    out.write("  shape-rendering: crispEdges;\n")
    out.write("}\n")
    out.write("\n")
    out.write(".axis .tick line {\n")
    out.write("  stroke-width: 1;\n")
    out.write("  stroke: rgba(0, 0, 0, 0.2);\n")
    out.write("}\n")
    out.write("\n")
    out.write(".axisHorizontal path{\n")
    out.write("  fill: none;\n")
    out.write("}\n")
    out.write("\n")
    out.write(".axisHorizontal line {\n")
    out.write("  fill: none;\n")
    out.write("  stroke: #000;\n")
    out.write("  shape-rendering: crispEdges;\n")
    out.write("}\n")
    out.write("\n")
    out.write(".axisHorizontal .tick line {\n")
    out.write("  stroke-width: 1;\n")
    out.write("  stroke: rgba(0, 0, 0, 0.2);\n")
    out.write("}\n")
    out.write("\n")
    out.write(".bar {\n")
    out.write("  fill: steelblue;\n")
    out.write("  fill-opacity: .9;\n")
    out.write("}\n")
    out.write("\n")
    out.write(".x.axis path {\n")
    out.write("  display: none;\n")
    out.write("}\n")
    out.write("</style>\n")
    out.write("<body>\n")
    out.write("\n")
    out.write("<script src=\"http://d3js.org/d3.v3.min.js\"></script>\n")
    out.write("<script>\n")
    out.write("\n")
    out.write("var margin = {top: (parseInt(d3.select('body').style('width'), 10)/10), right: (parseInt(d3.select('body').style('width'), 10)/20), bottom: (parseInt(d3.select('body').style('width'), 10)/5), left: (parseInt(d3.select('body').style('width'), 10)/20)},\n")
    out.write("    width = parseInt(d3.select('body').style('width'), 10) - margin.left - margin.right,\n")
    out.write("    height = parseInt(d3.select('body').style('height'), 10) - margin.top - margin.bottom;\n")
    out.write("\n")
    out.write("var x0 = d3.scale.ordinal()\n")
    out.write("    .rangeRoundBands([0, width], .1);\n")
    out.write("\n")
    out.write("var x1 = d3.scale.ordinal();\n")
    out.write("\n")
    out.write("var y = d3.scale.linear()\n")
    out.write("    .range([height, 0]);\n")
    out.write("\n")
    out.write("var colorRange = d3.scale.category20();\n")
    out.write("var color = d3.scale.ordinal()\n")
    out.write("    .range(colorRange.range());\n")
    out.write("\n")
    out.write("var xAxis = d3.svg.axis()\n")
    out.write("    .scale(x0)\n")
    out.write("    .orient(\"bottom\");\n")
    out.write("\n")
    out.write("var yAxis = d3.svg.axis()\n")
    out.write("    .scale(y)\n")
    out.write("    .orient(\"left\")\n")
 #   out.write("    .tickFormat(d3.format(\".2s\"));\n")
    out.write("\n")
    out.write("var divTooltip = d3.select(\"body\").append(\"div\").attr(\"class\", \"toolTip\");\n")
    out.write("\n")
    out.write("var svg = d3.select(\"body\").append(\"svg\")\n")
    out.write("    .attr(\"width\", width + margin.left + margin.right)\n")
    out.write("    .attr(\"height\", height + margin.top + margin.bottom)\n")
    out.write("    .append(\"g\")\n")
    out.write("    .attr(\"transform\", \"translate(\" + margin.left + \",\" + margin.top + \")\");\n")
    out.write("\n")

    out.write("dataset = [\n")
    info = data.readline()
    label = info.split(',')[0].strip('\"')
    count = 0
    for line in data:
        count += 1
        write_string = "    {"
        write_string += (label + ":\"" + line.rstrip().split(',')[0] + "\", \"")
        for i in range(len(info.split(',')[1:])):
            write_string += (info.rstrip().split(',')[i+1] + "\":")
            write_string += (line.rstrip().split(',')[i+1] + ", \"")
        write_string = write_string[1:-3]
        if count < num_lines:
            write_string += "},\n"
        else:
            write_string += "}\n"
        out.write(write_string)
    out.write("];\n")


    out.write("\n")
    out.write("var options = d3.keys(dataset[0]).filter(function(key) { return key !== \"label\"; });\n")
    out.write("dataset.forEach(function(d) {\n")
    out.write("    d.valores = options.map(function(name) { return {name: name, value: +d[name]}; });\n")
    out.write("});\n")
    out.write("\n")
    out.write("x0.domain(dataset.map(function(d) { return d.label; }));\n")
    out.write("x1.domain(options).rangeRoundBands([0, x0.rangeBand()]);\n")
    out.write("y.domain([0, d3.max(dataset, function(d) { return d3.max(d.valores, function(d) { return d.value; }); })]);\n")
    out.write("\n")
    out.write("svg.append(\"g\")\n")
    out.write("    .attr(\"class\", \"x axis\")\n")
    out.write("    .attr(\"transform\", \"translate(0,\" + height + \")\")\n")
    out.write("    .call(xAxis)\n")
    out.write("    .selectAll(\"text\")\n")
    out.write("      .style(\"text-anchor\", \"end\")\n")
    out.write("      .attr(\"dx\", \"-.8em\")\n")
    out.write("      .attr(\"dy\", \".15em\")\n")
    out.write("      .attr(\"transform\", function(d) {return \"rotate(-65)\" });\n")
    out.write("\n")
    out.write("svg.append(\"g\")\n")
    out.write("    .attr(\"class\", \"y axis\")\n")
    out.write("    .call(yAxis)\n")
    out.write("    .append(\"text\")\n")
    out.write("    .attr(\"transform\", \"rotate(-90)\")\n")
    out.write("    .attr(\"y\", 6)\n")
    out.write("    .attr(\"dy\", \".71em\")\n")
    out.write("    .style(\"text-anchor\", \"end\")\n")
    out.write("    .text(\"# of commits\");\n")
    out.write("\n")
    out.write("var bar = svg.selectAll(\".bar\")\n")
    out.write("    .data(dataset)\n")
    out.write("    .enter().append(\"g\")\n")
    out.write("    .attr(\"class\", \"rect\")\n")
    out.write("    .attr(\"transform\", function(d) { return \"translate(\" + x0(d.label) + \",0)\"; });\n")
    out.write("\n")
    out.write("bar.selectAll(\"rect\")\n")
    out.write("    .data(function(d) { return d.valores; })\n")
    out.write("    .enter().append(\"rect\")\n")
    out.write("    .attr(\"width\", x1.rangeBand())\n")
    out.write("    .attr(\"x\", function(d) { return x1(d.name); })\n")
    out.write("    .attr(\"y\", function(d) { return y(d.value); })\n")
    out.write("    .attr(\"value\", function(d){return d.name;})\n")
    out.write("    .attr(\"height\", function(d) { return height - y(d.value); })\n")
    out.write("    .style(\"fill\", function(d) { return color(d.name); });\n")
    out.write("\n")
    out.write("bar\n")
    out.write("    .on(\"mousemove\", function(d){\n")
    out.write("        divTooltip.style(\"left\", d3.event.pageX+10+\"px\");\n")
    out.write("        divTooltip.style(\"top\", d3.event.pageY-25+\"px\");\n")
    out.write("        divTooltip.style(\"display\", \"inline-block\");\n")
    out.write("        var x = d3.event.pageX, y = d3.event.pageY\n")
    out.write("        var elements = document.querySelectorAll(':hover');\n")
    out.write("        l = elements.length\n")
    out.write("        l = l-1\n")
    out.write("        elementData = elements[l].__data__\n")
    out.write("        divTooltip.html((d.label)+\"<br>\"+elementData.name+\"<br>\"+elementData.value+\"%\");\n")
    out.write("    });\n")
    out.write("bar\n")
    out.write("    .on(\"mouseout\", function(d){\n")
    out.write("        divTooltip.style(\"display\", \"none\");\n")
    out.write("    });\n")
    out.write("\n")
    out.write("var legend = svg.selectAll(\".legend\")\n")
    out.write("    .data(options.slice())\n")
    out.write("    .enter().append(\"g\")\n")
    out.write("    .attr(\"class\", \"legend\")\n")
    out.write("    .attr(\"transform\", function(d, i) { return \"translate(0,\" + i * 20 + \")\"; });\n")
    out.write("\n")
    out.write("legend.append(\"rect\")\n")
    out.write("    .attr(\"x\", width - 18)\n")
    out.write("    .attr(\"width\", 18)\n")
    out.write("    .attr(\"height\", 18)\n")
    out.write("    .style(\"fill\", color);\n")
    out.write("\n")
    out.write("legend.append(\"text\")\n")
    out.write("    .attr(\"x\", width - 24)\n")
    out.write("    .attr(\"y\", 9)\n")
    out.write("    .attr(\"dy\", \".35em\")\n")
    out.write("    .style(\"text-anchor\", \"end\")\n")
    out.write("    .text(function(d) { return d; });\n")
    out.write("\n")
    out.write("</script>\n")
    out.write("</body>\n")

    out.close()
    data.close()
