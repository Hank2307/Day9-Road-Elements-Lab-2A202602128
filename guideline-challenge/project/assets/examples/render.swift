// Render deterministic annotation diagrams from the original photographs and polygon coordinates.
// Run from the repository root: swift guideline-challenge/project/assets/examples/render.swift
import AppKit
import Foundation

struct Polygon: Decodable {
    let area_type: String
    let needs_review: Bool
    let points: [[Double]]
}
struct Badge: Decodable { let text: String; let x: Double; let y: Double }
struct Callout: Decodable { let text: String; let x: Double; let y: Double; let anchor: [Double] }
struct Sample: Decodable {
    let id: String
    let width: Int
    let height: Int
    let polygons: [Polygon]
    let badges: [Badge]
    let callouts: [Callout]
    let notes: [String]
}
struct Annotations: Decodable { let images: [Sample] }
let folder = URL(fileURLWithPath: #filePath).deletingLastPathComponent()
let dataset = folder.appendingPathComponent("../../../data/bdd100k").standardized
let samples = try JSONDecoder().decode(Annotations.self, from: Data(contentsOf: folder.appendingPathComponent("annotations.json")))
let direct = NSColor(srgbRed: 0.06, green: 0.80, blue: 0.48, alpha: 1)
let alternative = NSColor(srgbRed: 0.12, green: 0.56, blue: 1, alpha: 1)
let review = NSColor(srgbRed: 1, green: 0.70, blue: 0.18, alpha: 1)
let ink = NSColor(srgbRed: 0.045, green: 0.075, blue: 0.12, alpha: 1)
func text(_ value: String, _ x: Double, _ y: Double, _ size: Double = 21, _ color: NSColor = .white, bold: Bool = false) {
    let font = bold ? NSFont.boldSystemFont(ofSize: size) : NSFont.systemFont(ofSize: size)
    (value as NSString).draw(at: NSPoint(x:x, y:y), withAttributes: [.font:font, .foregroundColor:color])
}
func box(_ x: Double, _ y: Double, _ w: Double, _ h: Double, _ color: NSColor) {
    color.setFill()
    NSBezierPath(roundedRect:NSRect(x:x,y:y,width:w,height:h), xRadius:8,yRadius:8).fill()
}
for sample in samples.images {
    let width = sample.width, height = sample.height + 184
    guard let photo = NSImage(contentsOf: dataset.appendingPathComponent("\(sample.id).jpg")),
          let bitmap = NSBitmapImageRep(bitmapDataPlanes:nil,pixelsWide:width,pixelsHigh:height,bitsPerSample:8,samplesPerPixel:4,hasAlpha:true,isPlanar:false,colorSpaceName:.deviceRGB,bytesPerRow:0,bitsPerPixel:0),
          let base = NSGraphicsContext(bitmapImageRep:bitmap) else { fatalError("Cannot load/render \(sample.id)") }
    NSGraphicsContext.saveGraphicsState()
    let cg = base.cgContext
    cg.translateBy(x:0,y:CGFloat(height))
    cg.scaleBy(x:1,y:-1)
    NSGraphicsContext.current = NSGraphicsContext(cgContext:cg,flipped:true)
    ink.setFill()
    NSRect(x:0,y:0,width:width,height:height).fill()
    text("\(sample.id)  ·  NHÃN THỬ",24,19,27,.white,bold:true)
    box(385,23,20,20,direct); text("direct",416,18,24)
    box(541,23,20,20,alternative); text("alternative",572,18,24)
    box(764,23,20,20,review); text("Biên đứt: cần kiểm tra",796,19,22)
    photo.draw(in:NSRect(x:0,y:72,width:width,height:sample.height),from:.zero,operation:.copy,fraction:1,respectFlipped:true,hints:nil)
    for polygon in sample.polygons {
        precondition(polygon.points.count >= 3)
        let path = NSBezierPath()
        for (index, point) in polygon.points.enumerated() {
            precondition(point.count == 2 && point[0] >= 0 && point[0] < Double(width) && point[1] >= 0 && point[1] < Double(sample.height))
            let at = NSPoint(x:point[0],y:point[1]+72)
            if index == 0 { path.move(to:at) } else { path.line(to:at) }
        }
        path.close()
        let color = polygon.area_type == "direct" ? direct : alternative
        color.withAlphaComponent(0.32).setFill(); path.fill()
        (polygon.needs_review ? review : color).setStroke()
        path.lineWidth = 3
        if polygon.needs_review { path.setLineDash([9,6],count:2,phase:0) }
        path.stroke()
    }
    for badge in sample.badges {
        let w: Double = badge.text == "direct" ? 98 : 160
        box(badge.x,badge.y+72,w,34,ink.withAlphaComponent(0.9))
        text(badge.text,badge.x+12,badge.y+74,23,badge.text == "direct" ? direct : alternative,bold:true)
    }
    for callout in sample.callouts {
        let font = NSFont.boldSystemFont(ofSize:21)
        let w = Double((callout.text as NSString).size(withAttributes:[.font:font]).width) + 24
        let line = NSBezierPath()
        line.move(to:NSPoint(x:callout.x+w/2,y:callout.y+72+36))
        line.line(to:NSPoint(x:callout.anchor[0],y:callout.anchor[1]+72))
        NSColor.white.withAlphaComponent(0.92).setStroke(); line.lineWidth=2; line.stroke()
        NSColor.white.setFill()
        NSBezierPath(ovalIn:NSRect(x:callout.anchor[0]-4,y:callout.anchor[1]+68,width:8,height:8)).fill()
        box(callout.x,callout.y+72,w,36,ink.withAlphaComponent(0.93))
        text(callout.text,callout.x+12,callout.y+77,21,.white,bold:true)
    }
    for (index, note) in sample.notes.enumerated() { text(note,24,Double(sample.height+88+index*29),21) }
    text("Minh họa theo guideline v1 · Chưa qua QA · Không phải ground truth BDD100K",24,Double(sample.height+151),17,NSColor.lightGray)
    NSGraphicsContext.restoreGraphicsState()
    guard let png = bitmap.representation(using:.png,properties:[:]) else { fatalError("PNG export failed") }
    let output = folder.appendingPathComponent("\(sample.id)-annotated.png")
    try png.write(to:output)
    print(output.path)
}
